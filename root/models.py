from django.db import models

class Testimonial(models.Model):
    image = models.ImageField(upload_to= 'root' , default='default_root.jpg')
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    def __str__(self):
        return self.title