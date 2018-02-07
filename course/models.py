from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class Course(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    langauge =
    title
    paid
    active
    price
    type choice = book, video, course
    level = advanced begineeer, inter
    expexted duration
    upvotes=
    tech =
