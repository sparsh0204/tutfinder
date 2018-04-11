from django.contrib import admin
from django.apps import apps

review = apps.get_app_config('review')

for model_name, model in review.models.items():
    admin.site.register(model)
