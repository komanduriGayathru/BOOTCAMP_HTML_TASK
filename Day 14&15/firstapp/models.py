from django.db import models


# Create your models here.
class Bootcamp_Candidate(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
