from django.shortcuts import render , HttpResponse , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout 
import time
from time import sleep
# from django.contrib.auth.forms import UserCreationForm
# from django.db import models



# Create your views here.
def home(request):
    return render(request, 'index.html')
def free_wifi(request):
    return render(request, 'free_wifi.html')
def own_a_router(request):
    return render(request, 'own_a_router.html')
def subscription_plans(request):
    return render(request, 'subscription_plans.html')
def handlesignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            messages.error(request,'password and confirm password should be same')
            return HttpResponseRedirect('/home/')
        else:
            myuser=User.objects.create_user(username, email, pass1)               
            myuser.first_name=fname 
            myuser.save()
            messages.success(request, 'account is created succefully')
            return HttpResponseRedirect('/home/')
           
def handlelogin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)
    User=authenticate(request,username=username , password=password)

    if User is not None:
        login(request, User)
        username=User.get_username
        messages.success(request, 'Loggedin succefully')
        return HttpResponseRedirect('/home/')
    else:
        messages.error(request,'wrong password or email')
        return HttpResponseRedirect('/home/')
    
def handlesignout(request):
    logout(request)
    messages.success(request, 'Loggedout succefully')
    return HttpResponseRedirect('/home/')
    return render(request, 'index.html')

    

