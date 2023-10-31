from django.urls import path
from . import views

urlpatterns = [
    path("",views.TicketListView.as_view(),name="home"),
    path("ticket_create",views.TicketCreateView.as_view(),name="ticket_create"),
    path("ticket_confirm_delete/<int:pk>/",views.TicketDeleteViews.as_view(),name="ticket_confirm_delete")
]