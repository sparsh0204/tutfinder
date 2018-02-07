from django.contrib import admin
from django.apps import apps

course = apps.get_app_config('course')

for model_name, model in course.models.items():
    admin.site.register(model)
