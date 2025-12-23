from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.db import models
from .users import User
from django.utils.translation import gettext_lazy as _

     
''' custom Profile model for our app'''
class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=None,
                              max_length=None, null=True, blank=True)
    
    description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.email} Profile'
    
#from django.db.models.signals import post_save
#from django.dispatch import receiver 
@receiver(post_save, sender=User)    # for signal conceptual trigger
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       Profile.objects.create(user=instance)





