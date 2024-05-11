"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Main (models.Model):
    intro = models.CharField(max_length=100)
    par1 = models.TextField()
### Second part of the index page
### This months events
class Events (models.Model):
    title = models.CharField(max_length=100)
    event = models.TextField()

    
    