from django.shortcuts import render,redirect
from django.urls import reverse

def notLoggedUser(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home:home'))
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func