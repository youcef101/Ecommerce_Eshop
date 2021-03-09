import json
from django.shortcuts import render
from product.models import *
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.models import ShopCart


# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    product_slider=Product.objects.order_by('?')[:4]
    latest_product=Product.objects.order_by('-id')[:4]
    picked_product=Product.objects.order_by('?')[:4]
    current_user=request.user
    shopcart=ShopCart.objects.filter(user_id=current_user.id)
    cartpro=shopcart.count()
    #page="home"
    context={
        #"page":page,
        "product_slider": product_slider,
        "latest_product":latest_product,
        "picked_product":picked_product,
        'cartpro':cartpro
        
    }
    return render(request,'home/index.html',context)

@login_required(login_url='accounts:login')
def category_products(request,id,slug):
   category = Category.objects.get(pk=id)
   products = Product.objects.filter(category_id=id)
   context={"products":products
                }
   return render(request,'home/category_products.html',context)

@login_required(login_url='accounts:login')
def product_detail(request,id,slug):
    product=Product.objects.get(pk=id)
    image=Images.objects.filter(product_id=id)
    comment =Comment.objects.filter(product_id=id,status=True)
    related_product=Product.objects.filter(category_id=product.category_id).exclude(pk=product.id).order_by('?')[:4]
    context={"product":product,
             "image":image ,
             "comment":comment,
             "related_product":related_product
            }
    return render(request,'home/product_detail.html',context)

def search(request):
    if request.method == 'GET': # check post
        form = searchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'product': products, 'query':query,
                       'category': category }
            return render(request, 'home/search_product.html', context)

    return HttpResponseRedirect('/')

def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)

        results = []
        for item in products:
            product_json = {}
            product_json = item.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)    

def about(request):
    setting=Setting.objects.get(pk=1)
    context={"setting":setting}
    return render(request,'home/about.html',context)

def contact(request):
    setting=Setting.objects.get(pk=1)
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
      form=contactMessage(request.POST)
      if form.is_valid():
          data=Contact()
          data.name=form.cleaned_data.get('name')
          data.email=form.cleaned_data.get('email')
          data.subject=form.cleaned_data.get('subject')
          data.message=form.cleaned_data.get('message')
          data.ip=request.META.get('REMOTE_ADDR')
          data.save()
          messages.success(request,'your message added successfully')
          return HttpResponseRedirect(url)

    
    context={"setting":setting}
    return render(request,'home/contact.html',context)