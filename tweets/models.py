from django.db import models


class Tweet(models.Model):
    '''
    To create object on the fly via the ./manage.py shell for testing models data:
    Tweet.objects.create(content="Ich bin Rafa", image="url")
    '''
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True)
    image = models.FileField(upload_to='images/', blank=True)
# Create your models here.
