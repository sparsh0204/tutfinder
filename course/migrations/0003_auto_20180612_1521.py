# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-12 15:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_auto_20180605_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, default='')),
                ('detail', models.TextField(blank=True, default='', null=True)),
                ('free', models.BooleanField(default=True)),
                ('level', models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='Select', max_length=20)),
                ('medium', models.CharField(choices=[('VIDEO', 'Video'), ('TEXT', 'Text')], default='Select', max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='raw_submitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='medium',
            field=models.CharField(choices=[('VIDEO', 'Video'), ('TEXT', 'Text')], default='Select', max_length=20),
        ),
    ]