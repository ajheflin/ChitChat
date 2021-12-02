from django.db import models
from django.db.models.fields import related

# Create your models here.
chat = "Chat"


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    chats = models.ManyToManyField(chat, null=True, blank=True)
    avatar_url = models.CharField(
        max_length=1000, default="https://i.stack.imgur.com/dr5qp.jpg")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    chat_image = models.CharField(
        max_length=1000, default="https://cdn-icons-png.flaticon.com/512/134/134914.png")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT)
    content = models.CharField(max_length=280)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.content
