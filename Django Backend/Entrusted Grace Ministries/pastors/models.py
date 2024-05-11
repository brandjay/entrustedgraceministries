from django.db import models

# Create your models here.
class Missionary (models.Model):
    #first name
    first_name = models.CharField(max_length=50)
    #last name
    last_name = models.CharField(max_length=50)
    #bio
    bio = models.TextField(max_length=1500)
    #date
    date = models.DateTimeField(auto_created=True)
    #uploads image to a folder named images
    image = models.ImageField(upload_to ='images/')