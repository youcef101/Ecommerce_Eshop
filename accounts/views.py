from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import Group,User
from .decorators import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from cart.models import *
from product.models import *

# Create your views here.
@notLoggedUser
def register(request):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=createNewUser(request.POST)
        if form.is_valid():
           username=form.cleaned_data.get('username')
           first_name=form.cleaned_data.get('first_name')
           last_name=form.cleaned_data.get('last_name')
           email=form.cleaned_data.get('email')
           password1=form.cleaned_data.get('password1')
           password2=form.cleaned_data.get('password2')
           messages.success(request,username +' Created Successfully')
           user=form.save()
           group=Group.objects.get(name='customer')
           user=user.groups.add(group)
           instance=User.objects.get(username=username,email=email)
           Customer.objects.create(user=instance)

           return HttpResponseRedirect(reverse('accounts:login'))
        else:
            messages.warning(request,'Password didnt match' )
            return HttpResponseRedirect(url)

    context={}
    return render(request,'auth/register.html',context)
@notLoggedUser
def userLogin(request):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            current_user =request.user
            customer=Customer.objects.get(user_id=current_user.id)
            request.session['userimage'] = customer.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,'username or password dont correct')
            return HttpResponseRedirect(url)
    context={}
    return render(request,'auth/login.html',context)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required(login_url='accounts:login') # Check login
def password_change(request):
    form = PasswordChangeForm(request.user)
    url=request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
          user = form.save()
          update_session_auth_hash(request, user)  # Important!
          messages.success(request, 'Your password was successfully updated!')
          return HttpResponseRedirect('/')
        else:
          messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
          return HttpResponseRedirect(url)
    
     
    context={'form':form}
    return render(request, 'auth/password_change.html',context)

def profile(request):
    current_user = request.user  # Access User Session information
    profile = Customer.objects.get(user_id=current_user.id)
    context={'profile':profile}
    return render(request,'auth/user_profile.html',context)

def user_update(request):
    url=request.META.get('HTTP_REFERER')
    customer=request.user.customer
    user=request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=customer)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            messages.warning(request,'update error' )
            return HttpResponseRedirect(url)
    else:
       
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.customer) #"userprofile" model -> OneToOneField relatinon with user
        context = {'user_form': user_form,'profile_form': profile_form}
        return render(request, 'auth/user_update.html', context)

def user_order(request):
    current_user=request.user
    order=Order.objects.filter(user_id=current_user.id)
    context={'order':order}
    return render(request,'auth/user_order.html',context)

def user_comment(request):
    current_user=request.user
    comment=Comment.objects.filter(user_id=current_user.id)
    context={'comment':comment}
    return render(request,'auth/user_comment.html',context)

def user_orderdetail(request,id):
    
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'auth/user_order_detail.html', context)

def user_order_product(request):
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
               'order_product': order_product,
               }
    return render(request, 'auth/user_order_product.html', context)

def user_order_product_detail(request,id,oid):
    
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id,user_id=current_user.id)
    context = {
        
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'auth/user_order_detail.html', context)

def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect(reverse('accounts:user_comment'))