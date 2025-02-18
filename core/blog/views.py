from django.shortcuts import render 

# Create your views here.

def indexView(request):
    title="FBV_Index"
    context={ "title":title }
       
    return render(request, 'index.html', context)


