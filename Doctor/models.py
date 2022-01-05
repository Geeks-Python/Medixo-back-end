from django.db import models
from django.contrib.auth import get_user_model


class Doctor(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    speciality = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=30, verbose_name="Email Address")
    phone_number = models.CharField(unique=True, max_length=14,null=True,blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    building_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(get_user_model() , on_delete = models.CASCADE) 
    img = models.CharField(max_length=1000, blank=True, null=False, 
    default="https://www.jupiterhospital.com/uploadedfiles/gallery/1584607002_male-dummy.jpg")
    opening_hours = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor_id = models.ForeignKey(get_user_model() , on_delete = models.CASCADE) 
    patient_id = models.CharField(max_length=20, blank=True, null=True, default="") 
    patient_name = models.CharField(max_length=20, blank=True, null=True, default="")
    Doctor_name = models.CharField(max_length=20, blank=True, null=True, default="")
    hour = models.CharField(max_length=20, blank=True, default="")
    date = models.CharField(max_length=20, blank=True, default="")
    clinic_location = models.CharField(max_length=100, blank=True, default="")
    def __str__(self):
        return self.patient_name