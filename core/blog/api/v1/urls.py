from django.urls import path  
from . import views
# type: ignore  # noqa: F401



app_name = 'v1.urls'

urlpatterns = [
    # path('post/',views.postList, name='post-list'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:id>/',views.postDetail, name='post-detail'),

   
]

