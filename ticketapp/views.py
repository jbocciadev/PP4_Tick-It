from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team, Ticket
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


class TicketDetail(View):

    def get(self, request, ticket_id, *args, **kwargs):
        queryset = Ticket.objects.filter(id = ticket_id)
        ticket = get_object_or_404(queryset)

        return render(
            request,
            "ticketapp/ticket_detail.html",
            {
                'ticket': ticket,
            },
        )

