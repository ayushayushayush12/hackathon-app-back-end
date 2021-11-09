from django.db import models

# Create your models here.

class TeamProfile(models.Model):
    TeamId = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=1500)
    HSorColl = models.CharField(max_length=500)
    Names = models.CharField(max_length=1500)
    Schools = models.CharField(max_length=1500)
    Grades = models.CharField(max_length=500)
    Struggle = models.CharField(max_length=500)
    IdeaProject = models.CharField(max_length=1500)
    Location = models.CharField(max_length=500)
    ContactInfo = models.CharField(max_length=1500)
    PhoneNumber = models.CharField(max_length=500)

    
