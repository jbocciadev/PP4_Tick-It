from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team, Ticket
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    TicketUpdateForm, TicketForm, TicketStatusUpdateForm, TicketTeamUpdateForm, TicketMemberUpdateForm
)


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


class UpdateStatus(LoginRequiredMixin, View):
    def get(self, request, ticket_id, *args, **kwargs):
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if loggedUser.profile.role != 0:
            statusForm = TicketStatusUpdateForm(initial={
                'status': ticket.status})
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
        statusForm = TicketStatusUpdateForm(request.POST)
        if statusForm.is_valid():
            print(statusForm)
            # newStatus = statusForm.fields['status']
            # ticket = get_object_or_404(Ticket, id=ticket_id)
            # ticket.status = newStatus
            # ticket.save()
            statusForm.save()


class TicketDetail(LoginRequiredMixin, View):

    def get(self, request, ticket_id, *args, **kwargs):
        # renders the individual ticket only if the user created it or if the user is not a customer
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if loggedUser.profile.role != 0 or loggedUser.id == ticket.author.id:
            # Creating empty dict to store values
            staff_listing = {}
            teams = Team.objects.all().values()
            users = User.objects.all()
            #  Iterating through teams to create staff listing with keys:values
            for team in teams:
                staff_listing[team['name']] = []
                # Iterating through users to see if they are in team and add to listing
                for user in users:
                    user_teams = []
                    for i in user.profile.teams.values():
                        user_teams.append(i['name'])
                        # print(user_teams)
                    if str(team['name']) in user_teams:
                        staff_listing[team['name']].append(user)

            statusForm = TicketStatusUpdateForm(initial={
                'status': ticket.status},
                prefix='status')

            teamForm = TicketTeamUpdateForm(initial={
                'assigned_team': ticket.assigned_team},
                prefix='team')
            memberForm = TicketMemberUpdateForm(initial={
                'assigned_member': ticket.assigned_member},
                prefix='member',
                assigned_team=ticket.assigned_team)

            form = TicketUpdateForm(initial={
                'status': ticket.status,
                'assigned_team': ticket.assigned_team,
                'assigned_member': ticket.assigned_member,
            },
                assigned_team=ticket.assigned_team)

            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                    'staff_listing': staff_listing,
                    'form': form,
                    # 'statusForm': statusForm,
                    'teamForm': teamForm,
                    'memberForm': memberForm,
                },
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )

    # def post(self, request, ticket_id, *args, **kwargs):
        # print(request.POST)
        # form = TicketUpdateForm(request.POST)
        # if form.is_valid():
        #     form.save()

        # if 'status' in request.POST:
        #     postedStatusform = TicketStatusUpdateForm(request.POST)
        #     if postedStatusform.is_valid():
        #         statusForm.save()
        #     else:
        #         print(postedStatusform.errors.as_data())
        
        # form = TicketUpdateForm(request.POST)
        # print(form)
    
        # print("posted")

        # if form.is_valid():
            # print("valid form")
            # ticket = get_object_or_404(Ticket, id=ticket_id)
        #     ticket.status = form['status'].value()
        #     newTeam = Team.objects.filter(pk=form['assigned_team'].value())[0]
        #     ticket.assigned_team = newTeam
        #     if form['assigned_member'].value():
        #         newMember = User.objects.filter(pk=form['assigned_member'].value())[0]
        #         ticket.assigned_member = newMember
        #     ticket.save()
        # else:
        #     print("invalid form")
        #     print(form.errors.as_data())
            # print(f"from form: ${form['assigned_team']}")

        return redirect('TicketDetail', ticket_id=ticket_id)


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
