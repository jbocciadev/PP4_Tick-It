# Generated by Django 3.2.21 on 2023-10-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0003_alter_ticket_assigned_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='teams',
            field=models.ManyToManyField(blank=True, to='ticketapp.Team'),
        ),
    ]
