from django.contrib import admin
from django.urls import path,include
from bana import views
# from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/login/home/',views.home, name='home'),
    path('free_wifi',views.free_wifi, name='free_wifi'),
    path('own_a_router/',views.own_a_router, name='own_a_router'),
    path('subscription_plans/',views.subscription_plans, name='subscription_plans'),
    path('signup/',views.handlesignup, name='handlesignup'),
    path('login/',views.handlelogin, name='handlelogin'),
    path('signup/login/',views.handlelogin, name='handlelogin'),


#    path('', views.bana, name=''),

]
