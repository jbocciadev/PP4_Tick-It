from .models import Ticket, Team, Profile
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField, ChoiceField
from django.db.models import Q
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'content',)


class TicketUpdateForm(forms.ModelForm):
    teams = Team.objects.all()
    staff = Profile.objects.filter(~Q(role=0)).values('user')

    staff_list = []
    for i in staff:
        staff_list.append(i["user"])

    status = forms.ChoiceField(required=True, choices=[
        (0, "Open"),
        (1, "Assigned"),
        (2, "Parked"),
        (3, "Closed")])
    status.widget.attrs.update({'class': 'form-select'})

    assigned_team = forms.ModelChoiceField(queryset=Team.objects.all())
    assigned_team.widget.attrs.update({'class': 'form-select'})

    assigned_member = forms.ModelChoiceField(queryset=User.objects.filter(pk__in=staff_list), required=False)
    assigned_member.widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Ticket
        fields = ('status', 'assigned_team', 'assigned_member')