from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse("hello world")
    return render(request,'about.html')

def home(request):
    #return HttpResponse('welcome to home page')
    return render(request,'home.html')
