from django.shortcuts import render, HttpResponse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team
from django.contrib.auth.mixins import LoginRequiredMixin


# class TicketList(generic.ListView):

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('/ticket_list')
    else:
        return render(request, 'index.html')


class TicketList(LoginRequiredMixin, generic.ListView):
    redirect_field_name = '/accounts/login'
    model = Ticket
    queryset = Ticket.objects.prefetch_related('author')
    template_name = 'ticket_list.html'
    paginate_by = 10
