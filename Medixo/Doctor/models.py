from django.db import models

# Create your models here.

class Doctor(models.Model):
    email = models.EmailField(unique=True, max_length=20, verbose_name="Email Address")
    country = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
