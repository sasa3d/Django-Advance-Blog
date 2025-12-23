from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    BaseUserManager)

from django.utils.translation import gettext_lazy as _


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
        extra_fields.setdefault('is_verified', True)
        
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
    is_verified = models.BooleanField(default=False)
    
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