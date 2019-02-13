from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete="CASCADE")
    profile_image = models.ImageField(upload_to="profile_pics", blank=True)
    user_bio = models.TextField(blank=True)
    #Posts field that is many to one, inherants from our post application models

    def __str__(self):
        return self.user.username

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
