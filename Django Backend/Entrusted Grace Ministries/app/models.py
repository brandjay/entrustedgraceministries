"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Main (models.Model):
    intro = models.CharField(max_length=100)
    par1 = models.TextField()

    """ def __str__(self):
        return self.title """