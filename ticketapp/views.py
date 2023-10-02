from django.shortcuts import render, HttpResponse
from django.views import generic, View

# class TicketList(generic.ListView):

def landing_page(request):
    return render(request, 'ticketapp/index.html')


def tickets_list(request):
    return HttpResponse("List of tickets goes here!...")
