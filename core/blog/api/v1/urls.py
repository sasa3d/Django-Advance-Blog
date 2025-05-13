from django.urls import path
from . import views
# type: ignore  # noqa: F401



app_name = 'blog.api.v1.urls'

urlpatterns = [
    path('post/',views.postlist, name='post-list'),
   
]

