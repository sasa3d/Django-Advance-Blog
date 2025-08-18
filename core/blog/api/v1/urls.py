from django.urls import path  
from . import views  # noqa: F401
# type: ignore  # noqa: F401



app_name = 'v1.urls'

urlpatterns = [
    # path('post/', views.PostListView, name='post-list'),
    # path('post/<int:id>/',views.PostDetail, name='post-detail'),
    # path('post/',views.PostListView.as_view(), name='post-list'),
    # path('post/<int:id>/',views.PostDetail.as_view(), name='post-detail'), #= pk=id
    path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    # path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),
    path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),

]

