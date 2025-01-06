from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
    name = models.CharField(max_length=150)
    


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    type = models.ForeignKey(BlogType,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
