from django.shortcuts import render  # type: ignore # noqa: F401
from django.views.generic.base import TemplateView # type: ignore
from .models import Post  # noqa: F401
from django.shortcuts import redirect  # type: ignore # noqa: F401
from django.views.generic.base import RedirectView  # type: ignore
from django.views.generic import ListView , DetailView, FormView, CreateView # type: ignore # noqa: F401
from django.views.generic import UpdateView  , DeleteView   # type: ignore
#from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin # type: ignore # noqa: F401

from django.shortcuts import get_object_or_404 # type: ignore
from .forms import PostForm  # noqa: F401



#from django.views.generic.base import TemplateView
class indexView(TemplateView):  # noqa: F811
    ''' this is a class based view to show the index page'''
    template_name = "index.html"
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title="SaberSASA_SORNA"
        context["title"] = title
        context["content"] = "This is a class based view"
        context["posts"] = Post.objects.all()
        return context
    
# Function based view(FBV) for redirect a template 
""" 
from django.shortcuts import redirect
def RedirectToMaktab(request):
    ''' this is a function based view to redirect to maktabkhooneh.com'''
    return redirect("https://www.maktabkhooneh.com/") 
"""

# from django.views.generic.base import RedirectView  # noqa: E402
class RedirectToMaktab(RedirectView):  # noqa: F811
    ''' this is a class based view to redirect to maktabkhooneh.com'''
    url = "https://www.maktabkhooneh.com/"
    
    def get_redirect_url(self, *args, **kwargs):
         post = get_object_or_404(Post, pk=kwargs['pk'])
         print(post) 
         return super().get_redirect_url(*args, **kwargs)
         

# Class based view (CBV) for show a list of posts
#from django.views.generic.list import ListView
#from django.contrib.auth.mixins import loginRequiredMixin
class PostListView(PermissionRequiredMixin ,LoginRequiredMixin, ListView):  # noqa: F821
    context_object_name = "posts"
    #model = Post 
    #queryset = Post.objects.all()
    permission_required = "blog.view_post"
    # def get_permission_required(self):
    #     # می‌توانید در اینجا تصمیم بگیرید که چه مجوزهایی لازم است
    #     return ['blog.view_post']
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        #posts = Post.objects.filter(status=False)
        return posts
    
    paginate_by = 2
    ordering = ["-id"]
    
#django.views.generic.detail import DetailView
class PostDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Post
    # template_name = "blog/post_detail.html"
    # context_object_name = "post"
    permission_required = "blog.view_post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Post Detail"
        return context     

#from django.views.generic.edit import FormView     
""" class PostCreateView(FormView):
    model = Post
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"
    
    def  form_valid(self, form):
        form.save()
        return super().form_valid(form) 
 """
#from django.views.generic.edit import CreateView   
class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Post
    '''fields = ["title", "content", "status", "author",
              "category","published_date"]
    '''
    permission_required = "blog.view_post"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.object.author = self.request.user
        return super().form_valid(form)


# from django.views.generic.edit import UpdateView    
class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    permission_required = "blog.view_post"
    #template_name = "blog/post_edit.html"
    success_url = "/blog/post/"
    
# from django.views.generic.edit import DeleteView
#from django.urls import reverse_lazy
class PostDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    model = Post
    #success_url = reverse_lazy("author-list") 
    permission_required = "blog.view_post"
    success_url = "/blog/post/"   
    
    
    
        
    
