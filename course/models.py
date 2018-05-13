from django.db import models
from technology.models import Technology
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField #does not contain upload option for us in Images
from ckeditor_uploader.fields import  RichTextUploadingField #for adding upload from our own server in CKEDITOR

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    url = models.URLField(default='', blank=True)
#    langauge =
    title = models.CharField(max_length=255, blank=True, null=True)
    detail = RichTextUploadingField()
    free = models.BooleanField(default=True, blank=False)
#    active
#    price
#    type choice = book, video, course
    LEVEL = (('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
               ('ADVANCED', 'Advanced'))
    level = models.CharField(choices=LEVEL, default='Select', max_length=20, blank=False)
#    advanced begineeer, inter
#    expexted duration
    upvotes = models.IntegerField(blank=True, null=True)
    tech = models.ForeignKey(Technology, default= None , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

#    def get_absolute_url(self):

    def __str__(self):
        return (self.title + str(self.tech))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)