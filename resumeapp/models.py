from django.db import models

# Create your models here.
class resume(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    about=models.TextField(max_length=2000)
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    previous=models.TextField(max_length=1000)
    skills=models.TextField(max_length=1000)