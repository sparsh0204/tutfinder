from django.contrib import admin
from django.apps import apps

user = apps.get_app_config('user')

for model_name, model in user.models.items():
    admin.site.register(model)
