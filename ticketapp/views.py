from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Ticket, User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    TicketForm,
    TicketStatusUpdateForm,
    TicketTeamUpdateForm,
    TicketMemberUpdateForm
)


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('/ticket_list')
    else:
        return render(request, 'index.html')


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


class TicketList(LoginRequiredMixin, generic.ListView):
    # Returns list of tickets.
    # If user is staff, only return open tickets. If user is customer,
    # only return user-created tickets
    redirect_field_name = '/accounts/login'
    model = Ticket

    def get_queryset(self):
        loggedUser = self.request.user

        if loggedUser.profile.role == 0:
            # print('customer')
            return Ticket.objects.filter(Q(author=loggedUser)).prefetch_related('author').order_by('-created_on')
        else:
            # print('staff')
            return Ticket.objects.filter(~Q(status=3)).prefetch_related('author').order_by('-created_on')

    # Adding loggedUser data to the context to limit the fields displayed by the view
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['loggedUser'] = self.request.user
        return context

    template_name = 'ticket_list.html'
    paginate_by = 15


class TicketDetail(LoginRequiredMixin, View):

    def get(self, request, ticket_id, *args, **kwargs):
        # renders the individual ticket only if the user created it or if the user is staff/manager
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if loggedUser.profile.role != 0 or loggedUser.id == ticket.author.id:

            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                },
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )


class UpdateStatus(LoginRequiredMixin, View):
    def get(self, request, ticket_id, *args, **kwargs):
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if loggedUser.profile.role != 0:
            statusForm = TicketStatusUpdateForm(initial={
                'status': ticket.status,
                'author': ticket.author,
                'assigned_member': ticket.assigned_member}
                )
            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                    'statusForm': statusForm,
                }
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )

    def post(self, request, ticket_id, *args, **kwargs):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        statusForm = TicketStatusUpdateForm(request.POST, instance=ticket)
        if statusForm.is_valid():
            # print("statusForm valid")
            # print(statusForm)
            statusForm.save()
            return redirect('TicketDetail', ticket_id=ticket_id)

        else:
            # print("statusForm not valid")
            # print(statusForm)
            return redirect('TicketDetail', ticket_id=ticket_id)


class UpdateTeam(LoginRequiredMixin, View):
    def get(self, request, ticket_id, *args, **kwargs):
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if loggedUser.profile.role != 0:
            teamForm = TicketTeamUpdateForm(initial={
                'assigned_team': ticket.assigned_team,
                'author': ticket.author,
                'assigned_member': ticket.assigned_member})
            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                    'teamForm': teamForm,
                }
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )

    def post(self, request, ticket_id, *args, **kwargs):
        # print(f"teamForm submitted")
        ticket = get_object_or_404(Ticket, id=ticket_id)
        # print(ticket.author)
        teamForm = TicketTeamUpdateForm(request.POST, instance=ticket)
        if teamForm.is_valid():
            # print(f"teamForm valid")
            teamForm.save()
            return redirect('TicketDetail', ticket_id=ticket_id)

        else:
            # print(f"teamForm not valid")
            # print(teamForm)
            return redirect('TicketDetail', ticket_id=ticket_id)


class UpdateMember(LoginRequiredMixin, View):
    def get(self, request, ticket_id, *args, **kwargs):
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if loggedUser.profile.role != 0:
            memberForm = TicketMemberUpdateForm(initial={
                'assigned_team': ticket.assigned_team,
                'author': ticket.author,
                'assigned_member': ticket.assigned_member},
                assigned_team=ticket.assigned_team)
            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                    'memberForm': memberForm,
                }
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )

    def post(self, request, ticket_id, *args, **kwargs):
        # print(f"memberForm submitted")
        ticket = get_object_or_404(Ticket, id=ticket_id)
        # print(ticket.author)
        memberForm = TicketMemberUpdateForm(
            request.POST,
            instance=ticket,
            assigned_team=ticket.assigned_team
            )
        if memberForm.is_valid():
            # print(f"memberForm valid")
            memberForm.save()
            return redirect('TicketDetail', ticket_id=ticket_id)

        else:
            # print(f"memberForm not valid")
            # print(memberForm)
            return redirect('TicketDetail', ticket_id=ticket_id)
