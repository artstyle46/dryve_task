# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20160327_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='user_inventory',
            new_name='user',
        ),
    ]