from django.shortcuts import render  # noqa: F401
from django.views.generic.base import TemplateView
from .models import Post  # noqa: F401
from django.shortcuts import redirect  # noqa: F401
from django.views.generic.base import RedirectView  
from django.shortcuts import get_object_or_404



# Function based view (FBV) for show a template indexView
""" def indexView(request):
    ''' this is a function based view to show the index page'''
    title="FBV_Index"
    context={ "title":title }
       
    return render(request, 'index.html', context) 
"""

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
         
         
         

    
    


