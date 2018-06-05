from django.contrib import admin
from django.apps import apps

track_course = apps.get_app_config('track_course')

for model_name, model in track_course.models.items():
    admin.site.register(model)
