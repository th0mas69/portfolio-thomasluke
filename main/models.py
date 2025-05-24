from django.db import models

# Create your models here.
from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    duration = models.CharField(max_length=100)
    description = models.TextField()

class Education(models.Model):
    degree = models.CharField(max_length=250)
    institution = models.CharField(max_length=250)
    duration = models.CharField(max_length=100)

class Profile(models.Model):
    address = models.TextField()
    github_url = models.URLField()
    linkedin_url = models.URLField()
