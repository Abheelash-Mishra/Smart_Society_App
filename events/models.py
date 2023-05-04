from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.TextField(default="New Event!")
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    flat_no = models.TextField()
