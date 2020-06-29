from django.shortcuts import render
from .models import Contact
from django.shortcuts import HttpResponse, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model  # gets the user_model django  default or your own custom
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
# html pages
def home(request):
    return  render(request,'home/home.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        phon=request.POST['phon']
        email=request.POST['email']
        content=request.POST['content']
        if len(name)<2 or  len(phon)<10 or len(email)<3 or len(content)<4:
            messages.error(request, 'Plz enter valid entry')
        else:
           contact=Contact(name=name,email=email,phon=phon,content=content)
           messages.success(request, 'Form Submitted')
           contact.save()
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')

# aps is
def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # check for erros
        if len(username)>10:
            messages.success(request, 'username must be under 10 characters ')
            return redirect('home')
        if not username.isalnum() :
            messages.success(request, 'username should only contain  characters  and numbers')
            return redirect('home')
        if pass1!=pass2:
            messages.success(request, 'passwords do not match')
            return redirect('home')
        #create user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'your acount has been successfully created')
        return redirect('home')
    else:
        return HttpResponse('404-not fond')

    # Class to permit the athentication using email or username
def handleLogin(request):
    username=request.POST['loginusername']
    pwd=request.POST['loginpass']
    user=authenticate(username=username,password=pwd)  
    if user is not None:
            login(request,user)
            messages.success(request, 'login successfully')
            return redirect('home')

    else:
        messages.error(request, 'invalid credentilas ')
        return redirect('home')

        #else:
         #  return HttpResponse('404-not fond')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('home')
