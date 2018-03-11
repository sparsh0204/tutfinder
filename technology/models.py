from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

class Technology(models.Model):

    def tech_logo(instance, filename):
        return '/'.join(['Technology', ])
#    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
#    langauge =
    title = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True)
    doc_url = models.URLField(default='', blank=True)#<a href="{{ url }}">{{ url }}</a> Hint for html
    logo = models.ImageField(upload_to=tech_logo, blank=True,)
    logo_url = models.URLField(default='', blank=False)
    slug = models.SlugField(blank=True, unique=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Technology, self).save(*args, **kwargs)
class Versions(models.Model):
    tech = models.ForeignKey(Technology, on_delete=models.CASCADE, default=None)
    version = models.TextField()