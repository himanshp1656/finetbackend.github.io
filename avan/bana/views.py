from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
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
        email=request.POST.get('email1')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        myuser=User.objects.create_user(username, email, pass1)        
        myuser.save()
        #return HttpResponse('fuck')
        return redirect('login/')
        
    else:
        return HttpResponse('hell fuck')
    #     return redirect('home')
    # else:
    #     return HttpResponse('404-not found')
def handlelogin(request):
    email=request.POST.get('email')
    pass3=request.POST.get('pass3')
    User=authenticate(email=email , password=pass3)

    if User is not None:
        login(request, User)
        username=User.get_username
        HttpResponse('you are logged in')
        time.sleep(5)
        return redirect('home/')
        return render(request, 'index.html',{'username':username})
    else:
      #  messages.error('wrong password or email')
        return redirect('home/')

    

