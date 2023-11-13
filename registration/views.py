from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from core.models import Tech
from core.forms import TechForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "sign_up.html"

    def get_success_url(self) -> str:
        return reverse_lazy("login")
    
    def get_form(self, form_class = None):
        form = super(SignUpView,self).get_form()
    
        form.fields["username"].widget = forms.TextInput(attrs={"class":"form-control"})
        form.fields["password1"].widget = forms.PasswordInput(attrs={"class":"form-control"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={"class":"form-control"})

        return form

class ProfileUpdate(UpdateView):
    form_class = TechForm
    success_url = reverse_lazy("profile")
    template_name = "profile_form.html"

    def get_object(self):
        profile, created = Tech.objects.get_or_create(user=self.request.user)
        return profile