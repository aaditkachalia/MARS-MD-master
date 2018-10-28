from django.db import models
from django.urls import reverse

class Patient(models.Model):
    # address,contact,email
    patient_firstname = models.CharField(max_length=25)
    patient_surname = models.CharField(max_length=30)
    doctor = models.CharField(max_length=25)
    disease_type = models.CharField(max_length=100)
    patient_photo = models.FileField()
    affected_region_photo = models.FileField()
    terminal = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('hosp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.patient_firstname + " " +self.patient_surname



