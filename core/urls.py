from django.urls import path
from . import views

urlpatterns = [
    path("",views.TicketListView.as_view(),name="home"),
    path("ticket_create",views.TicketCreateView.as_view(),name="ticket_create"),
    path("ticket_confirm_delete/<int:pk>/",views.TicketDeleteView.as_view(),name="ticket_confirm_delete"),
    path("ticket_detail/<int:pk>/",views.TicketDetailView.as_view(),name="ticket_detail"),
    path("ticket_edite/<int:pk>/",views.TicketUpdateView.as_view(),name="ticket_edit"),

    path("tech_list",views.TechListView.as_view(),name="tech_list"),
    path("tech_create",views.TechCreateView.as_view(),name="tech_create"),
    path("tech_confirm_delete/<int:pk>/",views.TechDeleteView.as_view(),name="tech_confirm_delete"),
   
    path("tech_edite/<int:pk>/",views.TechUpdateView.as_view(),name="tech_edit"),
]