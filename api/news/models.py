from django.db import models

# Create your models here.

class news(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class register(models.Model):
    username= models.CharField(max_length=50)
    email =models.EmailField()
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
   
    def __str__(self):
        return self.username       