from django.db import models
from django.utils import timezone
from django.urls import reverse


class Clients(models.Model):

    client_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('clients')

# timezone.now I'm not using () beacuse I would not like yo execute this function() as yes
# Until execution


class Projects(models.Model):
    PEOJECT_STATUS_CHOICE = (
        ('', 'Select Status'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Complete', 'Complete'),
    )

    project_name = models.CharField(max_length=255)
    project_status = models.CharField(
        max_length=100, choices=PEOJECT_STATUS_CHOICE)
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
