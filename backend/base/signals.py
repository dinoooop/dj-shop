from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from base.views import product_views as views

def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email

pre_save.connect(updateUser, sender=User )
