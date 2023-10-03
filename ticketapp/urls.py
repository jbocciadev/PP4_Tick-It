from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('ticket_list/', views.TicketList.as_view(), name='TicketList'),
]
