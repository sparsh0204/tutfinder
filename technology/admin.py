from django.contrib import admin
from django.apps import apps

technology = apps.get_app_config('technology')

for model_name, model in technology.models.items():
    admin.site.register(model)
