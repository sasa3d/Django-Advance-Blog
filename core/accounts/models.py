from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    BaseUserManager)

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save 
from django.dispatch import receiver 

class UserManager(BaseUserManager):
    ''' custom user model manager'''
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,
        and password and extra data fields.
        """ 
        if not email:
            raise ValueError(_('Users must have an email address ("The Email must be set")'))
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ''' custom User model for our app'''
    email = models.EmailField(unique=True, max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    # تذکر: 
    #کسی که یا USER یا STAFF ی is_staff نباشد حق دسترسی به پنل ادمین را ندارد
    
    is_active = models.BooleanField(default=True)
    # is_verified = models.models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    """ 
     چونکه عامل USERNAME رو برای AUTHENTICATION
     , VERIFICATION حذف کرده ایم و ایمیل رو جایگزین نموده
     ایم پس باید ذکر  کنیم که شاخص کاری و نقش محور همان 
     E-MAIL میباشد و از این دستور استفاده مینماییم  ر USERNAME 
    """   
    
    REQUIRED_FIELDS = []   
    '''
     باید حتما                   
     در هنگام ساخت این کلاس فیلدهای مورد نیاز قرار داده شود 
     که در اینجا خالی ست چون  نیازمندیهای ما در این پروژه قرار
     است از طریق پروفایل تامین شوند
    '''
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __str__(self):
      return self.email

      
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
       
       
    
    
    
    