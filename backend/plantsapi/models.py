from django.db import models
from django.urls import reverse

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='plants/')
    instructions = models.CharField(max_length=1400)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name

class Request(models.Model):
    plant_name = models.CharField(max_length=100)
  
    def __str__(self):
        return self.plant_name