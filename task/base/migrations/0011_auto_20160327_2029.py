# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_inventory_bike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='inventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='user_inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
