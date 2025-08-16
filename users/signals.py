from django.db.models.signals import post_save 
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile 

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.update_or_create(user=instance,
#                                          address=instance.profile.address,
#                                          birth_date=instance.profile.birth_date,
#                                          contact_number =instance.profile.contact_number,
#                                          experience=instance.profile.experience,)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#    instance.profile.save()