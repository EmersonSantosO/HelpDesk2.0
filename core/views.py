from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import TicketForm, TechForm, SpecialityForm
from .models import *


class TicketListView(ListView):
    model = Ticket
    template_name = "home.html"

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket_form.html"
    success_url = reverse_lazy('home')

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = "ticket_confirm_delete.html"
    success_url = reverse_lazy("home")

class TicketDetailView(DetailView):
    model = Ticket
    template_name = "ticket_detail.html"

class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket_form.html"
    success_url = reverse_lazy("home")



class TechListView(ListView):
    model = Tech
    template_name = "tech_list.html"

class TechCreateView(CreateView):
    model = Tech
    form_class = TechForm
    template_name = "tech_form.html"
    success_url = reverse_lazy('home')

class TechDeleteView(DeleteView):
    model = Tech
    template_name = "tech_confirm_delete.html"
    success_url = reverse_lazy("home")

class TechUpdateView(UpdateView):
    model = Tech
    form_class = TechForm
    template_name = "tech_form.html"
    success_url = reverse_lazy("home")



class SpecialityListView(ListView):
    model = Speciality
    template_name = "speciality_list.html"

class SpecialityCreateView(CreateView):
    model = Tech
    form_class = SpecialityForm
    template_name = "speciality_form.html"
    success_url = reverse_lazy("speciality_list")

class SpecialityDeleteView(DeleteView):
    model = Speciality
    template_name = "speciality_confirm_delete.html"
    success_url = reverse_lazy("speciality_list")

class SpecialityUpdateView(UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = "speciality_form.html"
    success_url = reverse_lazy("speciality_list")

    