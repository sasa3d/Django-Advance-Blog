from django.db import models
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Post(models.Model):
    
    '''
    this is a class for post model to define all the fields for 
    Blog app. 
    '''
    image = models.ImageField(_("Image"), upload_to=None,
                              height_field=None, width_field=None,
                              null=True, blank=True)
    
    author = models.ForeignKey("User",    
                               on_delete=models.CASCADE)
    
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True ,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
    
