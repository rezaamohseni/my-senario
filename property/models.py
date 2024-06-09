from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Propertie(models.Model):
    image = models.ImageField(upload_to='property' , default = 'property_default.jpg')
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    rent = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    