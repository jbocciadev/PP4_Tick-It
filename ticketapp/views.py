from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team, Ticket
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TicketForm


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('/ticket_list')
    else:
        return render(request, 'index.html')


class TicketList(LoginRequiredMixin, generic.ListView):
    # Returns list of tickets.
    # If user is staff, only return open tickets. If user is customer,
    # only return user-created tickets
    redirect_field_name = '/accounts/login'
    model = Ticket

    def get_queryset(self):
        loggedUser = self.request.user

        if loggedUser.profile.role == 0:
            return Ticket.objects.filter(Q(author=loggedUser)).prefetch_related('author').order_by('-created_on')
        else:
            return Ticket.objects.filter(~Q(status=3)).prefetch_related('author').order_by('-created_on')

    template_name = 'ticket_list.html'
    paginate_by = 15


class TicketDetail(LoginRequiredMixin, View):

    def get(self, request, ticket_id, *args, **kwargs):
        # renders the individual ticket only if the user created it or if the user is not a customer
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if loggedUser.profile.role != 0 or loggedUser.id == ticket.author.id:
            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                },
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
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
