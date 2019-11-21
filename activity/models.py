from django.db import models
from django.utils import timezone
from account.models import Patient, Specialist


class History(models.Model):
    title = models.CharField(max_length=255, null=True)
    notes = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)


class Referral(models.Model):
    notes = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialist_from = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='source')
    specialist_to = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='target')


class Appointment(models.Model):
    title = models.CharField(max_length=255, null=True)
    notes = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, default='booked',
                              choices=[('booked', 'Booked'), ('confirmed', 'Confirmed')])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
