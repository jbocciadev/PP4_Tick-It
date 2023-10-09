from django.shortcuts import render, HttpResponse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team


# class TicketList(generic.ListView):

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('/ticket_list')
    else:
        return render(request, 'index.html')


class TicketList(generic.ListView):
    model = Ticket
    queryset = Ticket.objects.prefetch_related('author')
    template_name = 'ticket_list.html'
    paginate_by = 10
