from django.db import models
from technology.models import Technology
from course.models import Course
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

class Review(models.Model):
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField(max_length= 1000)
    upvotes = models.IntegerField(default=0)


#    def get_absolute_url(self):

    def __str__(self):
        return str(self.user) + str(self.course)