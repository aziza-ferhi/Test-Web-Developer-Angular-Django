from django.db import models

# Create your models here.
class Employee (models.Model):
    firstname = models.CharField(max_length=70, blank=False, default='')
    lastname = models.CharField(max_length=70, blank=False, default='')
    phonenumber = models.IntegerField(blank=False, default='')
    salary = models.FloatField(max_length=70, blank=False, default='')
    role  = models.CharField(max_length=70, blank=False, default='')
    department = models.CharField(max_length=70, blank=False, default='')
    joindate = models.CharField(max_length=70, blank=False, default='')

