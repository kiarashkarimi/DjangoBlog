from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('Home')
    return render(request, 'Home.html')
    
def about(request):
    # return HttpResponse('Hi There, I am Kiarash')س
    return render(request, 'about.html')
