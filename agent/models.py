from django.db import models
from django.contrib.auth.models import User
class Agent(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='agent' , default='defoulte_agent.jpg')
    score = models.IntegerField(default=0)
    description = models.TextField()
    phone = models.IntegerField(default=0000000000)
    email = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    x = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
        
    def __str__(self):
        return self.user.username
    