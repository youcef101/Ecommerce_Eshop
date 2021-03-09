from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
# Create your views here.
def detail(request):
    context={}
    return render(request,'product/product_detail.html',context)

def product(request):
    product=Product.objects.all()
    context={"product":product}
    return render(request,'product/product_list.html',context)


def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
        data = Comment()  # create relation with model
        data.subject = form.cleaned_data.get('subject')
        data.comment = form.cleaned_data.get('comment')
        data.rate = form.cleaned_data.get('rate')
        data.ip = request.META.get('REMOTE_ADDR')
        data.product_id=id
        current_user= request.user
        data.user_id=current_user.id
        data.save()  # save data to table
        messages.success(request, "Your review has ben sent. Thank you for your interest.")
       
        #return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
    
