from django.shortcuts import render
from  django.shortcuts import HttpResponse,render
# Create your views here.
from . import views
def blogHome(request):
    return  render(request,'blog/post.html')

def blogPost(request):
    return  HttpResponse("hello i am in in blogpost")
