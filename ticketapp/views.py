from django.shortcuts import render, HttpResponse
from django.views import generic, View
from .models import Ticket

# class TicketList(generic.ListView):

def landing_page(request):
    return render(request, 'ticketapp/index.html')


class TicketList(generic.ListView):
    model = Ticket
    queryset = Ticket.objects.values()
    template_name = 'ticket_list.html'
    paginate_by = 10
    
