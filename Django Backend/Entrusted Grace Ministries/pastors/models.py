from django.db import models

# Create your models here.
class Missionary (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_created=True)
    image = models.ImageField(upload_to ='images/')