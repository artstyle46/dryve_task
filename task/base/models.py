from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Item(models.Model):
#     item_name = models.CharField(max_length=500)
#     quantity = models.IntegerField(default=0)
#     price = models.FloatField()
#     def __unicode__(self):
#         return self.item_name

class Inventory(models.Model):
    scooty = models.IntegerField(default=0)
    bike = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.id

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    user_type = (
        ('V', 'Vendor'),
        ('S', 'Supervisor'),
        ('B', 'Buyer'),
    )
    userRole = models.CharField(max_length=1, choices=user_type, default='B')
    def __unicode__(self):
        return self.user.username

class SuperVisor(models.Model):
    vendor = models.ForeignKey(User, related_name='vendor')
    supervisor = models.ForeignKey(User, related_name='supervisor')
    def __unicode__(self):
        return self.supervisor.username