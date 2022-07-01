from statistics import mode
from django.db import models
from django.urls import reverse

# Create your models here.
class SFO(models.Model):
    gruppe = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    modul = models.CharField(max_length=255)
    mandag = models.CharField(blank=True, max_length=255)
    tirsdag = models.CharField(blank=True, max_length=255)
    onsdag = models.CharField(blank=True, max_length=255)
    torsdag = models.CharField(blank=True, max_length=255)
    fredag = models.CharField(blank=True, max_length=255)