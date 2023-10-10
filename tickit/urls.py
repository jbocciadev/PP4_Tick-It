
from django.contrib import admin
from django.urls import path, include
from ticketapp.views import TicketList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ticketapp.urls'), name='ticketapp_urls'),
    path('accounts/', include('allauth.urls')),
]
