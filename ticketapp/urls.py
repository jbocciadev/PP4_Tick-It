from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('ticket_list/', views.TicketList.as_view(), name='TicketList'),
    path('view/<ticket_id>', views.TicketDetail.as_view(), name="TicketDetail"),
    path('update_status/<ticket_id>', views.UpdateStatus.as_view(), name="UpdateStatus"),
    path('update_assignment/<ticket_id>', views.UpdateAssignment.as_view(), name="UpdateAssignment"),
    path('new_ticket/', views.NewTicket.as_view(), name="NewTicket"),
]
