from django.db import models

# Create your models here.
class Bootcamp_Candidate(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)



