from django.db import models

# Create your models here.
class Image(models.Model):
 objects = None
 photo = models.ImageField(upload_to="myimage")
 date = models.DateField(auto_now_add=True)