from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team, Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TicketForm


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


class TicketDetail(LoginRequiredMixin, View):

    def get(self, request, ticket_id, *args, **kwargs):
        queryset = Ticket.objects.filter(id=ticket_id)
        ticket = get_object_or_404(queryset)

        return render(
            request,
            "ticketapp/ticket_detail.html",
            {
                'ticket': ticket,
            },
        )


class NewTicket(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "ticketapp/new_ticket.html",
            {
                'ticket_form': TicketForm()
            },
        )

    def post(self, request, *args, **kwargs):
        ticket_form = TicketForm(data=request.POST)

        if ticket_form.is_valid():
            ticket_form.instance.author = request.user
            ticket = ticket_form.save(commit=False)
            ticket.save()
        else:
            ticket_form = TicketForm
        
        return redirect('/ticket_list')
