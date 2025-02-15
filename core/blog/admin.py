from django.contrib import admin 
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category'
                    , 'created_date', 'updated_date', 'published_date')
    # یا اگر می‌خواهید آنها را در فرم نمایش دهید
    # readonly_fields = ('created_date', 'updated_date', 'published_date')
    #یا اگر می‌خواهید آنها را به عنوان فیلد های خودتان نمایش دهید
    fields = ('title', 'author', 'status', 'category'
              , 'content', 'image', 'created_date', 'updated_date', 'published_date')
    


admin.site.register(Post, PostAdmin)
admin.site.register(Category)    