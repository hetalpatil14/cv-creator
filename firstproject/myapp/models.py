from email.headerregistry import Address
from django.db import models



# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images')
    qualification = models.TextField(max_length=60)
    skills = models.TextField(max_length=30)
    objective = models.TextField(max_length=100)
    experience= models.TextField(max_length=100)
    honor = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
   # video = models.FileField(upload_to='video'

def __str__self(self):
    return self.name
