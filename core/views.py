from django.forms.models import BaseModelForm
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView #Lista objetos desde una bd
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ticket, Tech
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'home.html')

# Create your views here.
@method_decorator(login_required, name='dispatch')
class TicketListView(ListView):
    model = Ticket
    #Opcional
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

@method_decorator(login_required, name='dispatch')
class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    context_object_name = 'ticket'

    def get_object(self,queryset=None):
        ticket = super().get_object(queryset)
        if ticket.tech == Tech.objects.get(user = self.request.user):
            return ticket
        else:
            raise Http404("No tiene permisos para ver este ticket")
@method_decorator(login_required, name='dispatch')
class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        tech_instance = Tech.objects.get(user = self.request.user)
        form.instance.tech = tech_instance
        self.object = form.save()
        response = super().form_valid(form)
        return response

@method_decorator(login_required, name='dispatch')
class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

@method_decorator(login_required, name='dispatch')
class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')