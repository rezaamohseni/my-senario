from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
     
class Blog(models.Model):
    image = models.ImageField(upload_to='blog' , default='default_blog.jpg')
    title = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    