from django.shortcuts import render 
from django.views.generic.base import TemplateView
from .models import Post  # noqa: F401


# Create your views here.

def indexView(request):
    ''' this is a function based view to show the index page'''
    title="FBV_Index"
    context={ "title":title }
       
    return render(request, 'index.html', context)

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
    
    
    


