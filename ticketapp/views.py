from django.shortcuts import render, HttpResponse
from django.views import generic, View

class TicketList(generic.ListView):

