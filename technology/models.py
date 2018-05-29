from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


def tech_logo(instance, filename):
    return '/'.join(['Images/Technology', instance.title])


class Technology(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    detail = models.TextField(blank=True)
    doc_url = models.URLField(default='', blank=True)  # <a href="{{ url }}">{{ url }}</a> Hint for html
    logo = models.ImageField(upload_to=tech_logo, blank=True,)
    logo_url = models.URLField(default='', blank=True)
    course_count = models.IntegerField(default=0, blank=True)
    # category = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Technology, self).save(*args, **kwargs)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Technology.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_technology_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_technology_receiver, sender=Technology)

# class Versions(models.Model):
#     tech = models.ForeignKey(Technology, on_delete=models.CASCADE, default=None)
#     version = models.TextField()