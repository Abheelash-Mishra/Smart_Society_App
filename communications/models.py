from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    dislikes = models.ManyToManyField(User, blank=True, related_name="dislikes")

class Comment(models.Model):
    comment_body = models.TextField()
    comment_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name="user", related_name="profile", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank= True, null=True)
    birthday = models.DateField(blank= True, null=True)
    picture = models.ImageField(upload_to="uploads/profile_pic", default="uploads/profile_pic/default_PP.jpg", blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    flat_no = models.CharField(max_length=6, default="N/A")
    contact_no = models.CharField(max_length=13, default="N/A")


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()