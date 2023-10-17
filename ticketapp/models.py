from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Declaring models


# Team model

class Team(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


# Expanding Django default user model with 1-1 relatopnship on Profile.user

ROLE = (
    (0, "Customer"),
    (1, "Staff"),
    (2, "Manager")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    role = models.IntegerField(choices=ROLE, default=0)
    email = models.EmailField


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Ticket model
STATUS = (
    (0, "Open"),
    (1, "Assigned"),
    (2, "Parked"),
    (3, "Closed")
)


class Ticket(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        related_name='tickets_created',
        on_delete=models.SET('user_deleted')
    )
    created_on = models.DateTimeField(auto_now_add=True)
    assigned_team = models.ForeignKey(
        Team,
        related_name='team_assigned_tickets',
        on_delete=models.PROTECT,
        default=1
    )
    assigned_member = models.ForeignKey(
        User,
        related_name='user_assigned_tickets',
        on_delete=models.SET('user_deleted'),
        null=True,
        blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)
    closed_on = models.DateTimeField(blank=True, null=True)
