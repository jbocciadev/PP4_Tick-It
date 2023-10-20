from .models import Ticket, Team, Profile
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField, ChoiceField
from django.db.models import Q
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):
    # Form to create ticket
    class Meta:
        model = Ticket
        fields = ('title', 'content',)


class TicketStatusUpdateForm(forms.ModelForm):
    # Form to update ticket status
    status = forms.ChoiceField(required=True, choices=[
        (0, "Open"),
        (1, "Assigned"),
        (2, "Parked"),
        (3, "Closed")])
    status.widget.attrs.update({'class': 'form-select',
                                'id': 'status_select'})
    
    class Meta:
        model = Ticket
        fields = ('status', 'author', 'assigned_member')


class TicketTeamUpdateForm(forms.ModelForm):
    # Form to update assigned team on ticket
    assigned_team = forms.ModelChoiceField(queryset=Team.objects.all())
    assigned_team.widget.attrs.update(
            {'class': 'form-select ticket-detail-form-select ticket-team-form-select',
                'id': 'team_select'})

    class Meta:
        model = Ticket
        fields = ('assigned_team', 'author',)


class TicketMemberUpdateForm(forms.ModelForm):
    # Form to update team member assignment, based on assigned team // https://stackoverflow.com/questions/1697702/how-to-pass-initial-parameter-to-djangos-modelform-instance

    def __init__(self, *args, **kwargs):
        assigned_team = kwargs.pop('assigned_team')
        profiles = Profile.objects.filter(teams=assigned_team)

        super(TicketMemberUpdateForm, self).__init__(*args, **kwargs)
        self.fields['assigned_member'] = forms.ModelChoiceField(
            blank=True,
            required=False,
            queryset=User.objects.filter(profile__in=profiles)
            )
        self.fields['assigned_member'].widget.attrs.update(
            {'class': 'form-select ticket-detail-form-select',
                'id': 'member_select'})

    class Meta:
        model = Ticket
        fields = ('assigned_member',)


class TicketUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        assigned_team = kwargs.pop('assigned_team')
        profiles = Profile.objects.filter(teams=assigned_team)

        super(TicketUpdateForm, self).__init__(*args, **kwargs)
        self.fields['assigned_member'] = forms.ModelChoiceField(
            blank=True,
            required=False,
            queryset=User.objects.filter(profile__in=profiles)
            )
        self.fields['assigned_member'].widget.attrs.update(
            {'class': 'form-select ticket-detail-form-select',
                'id': 'member_select'})

    status = forms.ChoiceField(required=True, choices=[
        (0, "Open"),
        (1, "Assigned"),
        (2, "Parked"),
        (3, "Closed")])
    status.widget.attrs.update(
            {'class': 'form-select ticket-detail-form-select',
                'id': 'status_select'})

    assigned_team = forms.ModelChoiceField(queryset=Team.objects.all())
    assigned_team.widget.attrs.update({'class': 'form-select',
                'id': 'team_select'})

    

    class Meta:
        model = Ticket
        fields = ('status', 'assigned_team', 'assigned_member')

            # assigned_member = forms.ModelChoiceField(queryset=User.objects.filter(pk__in=staff_list), required=False)
    # assigned_member.widget.attrs.update({'class': 'form-select'})