from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('ticket_list/', views.TicketList.as_view(), name='TicketList'),
    path('view/<ticket_id>', views.TicketDetail.as_view(), name="TicketDetail"),
]
