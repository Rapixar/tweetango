from django.db import models


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    image = models.FileField(upload_to='images/', blank=True) 
# Create your models here.
