from django.db.models.signals import post_save 
from django.contrib.auth.models import User, Group 
from .models import Viewer



def viewer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='viewer')
        instance.groups.add(group)
        full_name = instance.first_name + ' ' + instance.last_name
        print(full_name) 
        Viewer.objects.create(user = instance, name = full_name, email = instance.email,)
 
post_save.connect(viewer_profile, sender = User)
