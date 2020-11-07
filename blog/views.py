from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h2>My home page</h2>')


def home(request):
    return render(request, 'blog/home.html')



# def about(request):
#     return HttpResponse('<h2>My about page</h2>')    


def about(request):
    return render(request, 'blog/about.html')    