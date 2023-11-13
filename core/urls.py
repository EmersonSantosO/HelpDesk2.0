from django.urls import path
from .views import TicketListView,TicketCreateView,TicketDeleteView,TicketDetailView,TicketUpdateView

urlpatterns = [
    path("ticket_list/",TicketListView.as_view(),name="ticket_list"),
    path("ticket_create/",TicketCreateView.as_view(),name="ticket_create"),
    path("ticket_confirm_delete/<int:pk>/",TicketDeleteView.as_view(),name="ticket_confirm_delete"),
    path("ticket_detail/<int:pk>/",TicketDetailView.as_view(),name="ticket_detail"),
    path("ticket_edite/<int:pk>/",TicketUpdateView.as_view(),name="ticket_edit"),

]