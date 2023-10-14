from .models import Ticket, Team, Profile
from django import forms
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'content',)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status',)


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('assigned_team', 'assigned_member',)
