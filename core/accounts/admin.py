from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User ,Profile

# Register your models here.


class CostumUserAdmin(UserAdmin):
    '''
    this is a custom admin class for costum user model 
    '''
    model = User
    list_display = ['email', 'is_staff', 'is_superuser', 'is_active','is_verified']
    list_filter = ['email','is_staff', 'is_superuser', 'is_active', 'is_verified']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        ("Authentication", {
            'fields': (
                'email', 'password'
                )
            }
         ),
        ("Permissions", {
            'fields': (
                'is_staff', 'is_superuser', 'is_active', 'is_verified'
                )
            }
         ),
        
        ("Group Permissions", {
            'fields': (
                'groups', 'user_permissions'
                )
            }
         ),
        
        ("Important Dates", {
            'fields': (
                'last_login',
                )
            }
         ),
    )
    
    
    add_fieldsets = (
        ("For All Fields", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'is_staff', 'is_superuser',
                       'is_active', 'is_verified'
                       )}
         ),
    )
    
    
    
admin.site.register(Profile)
admin.site.register(User, CostumUserAdmin)