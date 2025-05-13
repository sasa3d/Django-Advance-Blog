from django.urls import path  # type: ignore
from . import views 
from django.urls import include  # type: ignore
# from django.views.generic import TemplateView
# from django.views.generic.base import RedirectView  # noqa: F401


app_name = "blog"

urlpatterns = [ 
    
     path("fbv-index/", views.indexView.as_view(), name="fbv-index"),  # CBV با استفاده از as_view()
   
        # اگر FBV استفاده شود:
        # path("fbv-index/", views.indexView, name="fbv-index"),

    path("cbv-index/", views.indexView.as_view(), name="cbv-index"),

    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    
    
    
#  path(
#         "go-to-maktabkhooneh/",
#         RedirectView.as_view(url="https://www.maktabkhooneh.com/"),  # noqa: F821
#         name="go-to-maktabkhooneh",
#     ),         
#path("go-to-index/", RedirectView.as_view(pattern_name="blog:cbv-index"), name="redirect-to-cbv_index"),
#path("go-to-maktab/<int:pk>/", views.RedirectToMaktab.as_view(), name="redirect-to-maktabkhooneh"),
    path("api/v1/", include("blog.api.v1.urls")),
]

    

