from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Ticket, Profile, Team, Ticket
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TicketUpdateForm, TicketForm


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
            print('customer')
            return Ticket.objects.filter(Q(author=loggedUser)).prefetch_related('author').order_by('-created_on')
        else:
            print('staff')
            return Ticket.objects.filter(~Q(status=3)).prefetch_related('author').order_by('-created_on')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['loggedUser'] = self.request.user
        return context

    template_name = 'ticket_list.html'
    paginate_by = 15


class TicketDetail(LoginRequiredMixin, View):

    def get(self, request, ticket_id, *args, **kwargs):
        # renders the individual ticket only if the user created it or if the user is not a customer
        loggedUser = request.user
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if loggedUser.profile.role != 0 or loggedUser.id == ticket.author.id:
            # Creating empty dict to store values
            staff_listing = {}
            teams = Team.objects.all()
            users = User.objects.all()

            #  Iterating through teams to create keys for dict
            for team in teams:
                staff_listing[team] = []
                # Iterating through users to see if they are in team and add to listing
                for user in users:
                    user_teams = []
                    for i in user.profile.teams.values():
                        user_teams.append(i['name'])
                    if str(team) in user_teams:
                        staff_listing[team].append(user)
            print(staff_listing)

            form = TicketUpdateForm(initial={
                'status': ticket.status,
                'assigned_team': ticket.assigned_team,
                'assigned_member': ticket.assigned_member,
            })

            return render(
                request,
                "ticketapp/ticket_detail.html",
                {
                    'ticket': ticket,
                    'user': loggedUser,
                    'staff_listing': staff_listing,
                    'form': form,
                },
            )
        else:
            return render(
                request,
                'ticketapp/no_access.html'
            )

    def post(self, request, ticket_id, *args, **kwargs):
        form = TicketUpdateForm(request.POST)
        print("posted")

        if form.is_valid():
            print("valid form")
            ticket = get_object_or_404(Ticket, id=ticket_id)
            ticket.status = form['status'].value()
            newTeam = Team.objects.filter(pk=form['assigned_team'].value())[0]
            ticket.assigned_team = newTeam
            if form['assigned_member'].value():
                newMember = User.objects.filter(pk=form['assigned_member'].value())[0]
                ticket.assigned_member = newMember
            ticket.save()
        else:
            print("invalid form")
            print(form.errors.as_data())
            print(f"from form: ${form['assigned_team']}")

        return redirect('TicketDetail', ticket_id=ticket_id)


# class UpdateStatus(LoginRequiredMixin, View):
#     def post(self, request, ticket_id, *args, **kwargs):
#         form = StatusForm(request.POST)

#         if form.is_valid():
#             ticket = get_object_or_404(Ticket, id=ticket_id)
#             ticket.status = form['status'].value()
#             ticket.save()

#         return redirect('TicketDetail', ticket_id=ticket_id)


# class UpdateAssignment(LoginRequiredMixin, View):
#     def post(self, request, ticket_id, *args, **kwargs):
#         form = AssignmentForm(request.POST)

#         if form.is_valid():
#             ticket = get_object_or_404(Ticket, id=ticket_id)
#             ticket.status = form['status'].value()
#             ticket.save()

#         return redirect('TicketDetail', ticket_id=ticket_id)

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
