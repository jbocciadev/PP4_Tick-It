from django.contrib import admin
from .models import Ticket, Team


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'assigned_team')
    search_fields = ('id', 'author')
    

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# admin.site.register(Ticket)
# admin.site.register(Team)
