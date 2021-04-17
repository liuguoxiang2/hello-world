# models.py
from django.db import models


# Create your models here.
class Django1(models.Model):
    name = models.CharField(max_length=20)

class user2(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=20)



class medicalRecord(models.Model):
    name = models.CharField(max_length=10)
    sex  = models.CharField(max_length=4)
    date = models.DateField()
    syndrome= models.CharField(max_length=20)
    source= models.CharField(max_length=20)
    combination= models.CharField(max_length=80)
    class Meta:
     unique_together = (("name","sex","combination","syndrome"),)