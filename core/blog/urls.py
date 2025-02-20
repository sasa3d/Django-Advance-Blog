from django.urls import path 
from . import views 
# from django.views.generic import TemplateView
# from django.views.generic.base import RedirectView  # noqa: F401


app_name = "blog"

urlpatterns = [ 
    path("fbv-index/", views.indexView, name="fbv-index"),
#path("cbv-index/", indexView, name="cbv-index"),
#path("cbv-index/", TemplateView.as_view(template_name="index.html", extra_context={"title":"CBV_Index"})),
    path("cbv-index/", views.indexView.as_view(), name="cbv-index"),
    path("post/", views.PostList.as_view(), name="post-list"), 
#  path(
#         "go-to-maktabkhooneh/",
#         RedirectView.as_view(url="https://www.maktabkhooneh.com/"),  # noqa: F821
#         name="go-to-maktabkhooneh",
#     ),         
#path("go-to-index/", RedirectView.as_view(pattern_name="blog:cbv-index"), name="redirect-to-cbv_index"),
    path("go-to-maktab/<int:pk>/", views.RedirectToMaktab.as_view(), name="redirect-to-maktabkhooneh"),
]