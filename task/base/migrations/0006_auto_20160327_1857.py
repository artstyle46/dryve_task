# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20160327_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='bike',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='scooty',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='inventory',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='base.Inventory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(to='base.Item'),
        ),
    ]