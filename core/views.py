from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import TicketForm
from .models import *


class TicketListView(ListView):
    model = Ticket
    template_name = "home.html"

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "ticket_form.html"
    success_url = reverse_lazy('home')

class TicketDeleteViews(DeleteView):
    model = Ticket
    template_name = "ticket_confirm_delete.html"
    success_url = reverse_lazy("home")
