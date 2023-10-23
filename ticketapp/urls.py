from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('ticket_list/', views.TicketList.as_view(), name='TicketList'),
    path('no_access', views.NoAccess, name="NoAccess"),
    path('view/<ticket_id>', views.TicketDetail.as_view(), name="TicketDetail"),
    path('new_ticket/', views.NewTicket.as_view(), name="NewTicket"),
    path('update_status/<ticket_id>', views.UpdateStatus.as_view(), name="UpdateStatus"),
    path('update_team/<ticket_id>', views.UpdateTeam.as_view(), name="UpdateTeam"),
    path('update_member/<ticket_id>', views.UpdateMember.as_view(), name="UpdateMember"),
    path('delete_ticket/<ticket_id', views.DeleteTicket.as_view(), name="DeleteTicket"),
]
