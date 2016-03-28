# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 21:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0012_auto_20160327_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperVisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]