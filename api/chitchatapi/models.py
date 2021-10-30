from django.db import models

# Create your models here.
class User(models.Model):
    name        = models.CharField(max_length=100)
    username    = models.CharField(max_length=100)
    email       = models.CharField(max_length=100)
    id          = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username

class Chat(models.Model):
    name        = models.CharField(max_length=100)
    id          = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name