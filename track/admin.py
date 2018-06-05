from django.contrib import admin
from django.apps import apps

track = apps.get_app_config('track')

for model_name, model in track.models.items():
    admin.site.register(model)
