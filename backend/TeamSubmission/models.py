from django.db import models

# Create your models here.

class TeamSubmission(models.Model):
    TeamId = models.AutoField(primary_key=True)
    VideoLink = models.CharField(max_length=500)
    GithubLink = models.CharField(max_length=500)
    ProjectIdea = models.CharField(max_length=1500)
    CodingLanguages = models.CharField(max_length=1500)
class Login2(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)



    
