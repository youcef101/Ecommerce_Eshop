from django.shortcuts import render
from product.models import *
from .models import *
from .forms import *
from accounts.models import Customer
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.crypto import get_random_string
# Create your views here.
def checkout(request):
    context={}
    return render(request,'cart/checkout.html',context)
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product= Product.objects.get(pk=id)

    checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id) # Check product in shopcart
    if checkinproduct:
        control = 1 # The product is in the cart
    else:
        control = 0 # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
               
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    cartpro=shopcart.count()
    total=0
    for item in shopcart:
        total += item.product.price * item.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'category':category,
             'total': total,
             'cartpro':cartpro
             }
    return render(request,'cart/shopcart_product.html',context)

def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect(reverse("cart:shopcart"))


def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for item in shopcart:
        total += item.product.price * item.quantity
      

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper() # random cod
            data.code =  ordercode
            data.save() #


            for item in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id # Order Id
                detail.product_id = item.product_id
                detail.user_id = current_user.id
                detail.quantity = item.quantity
                detail.price = item.product.price
                detail.amount = item.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                
                product = Product.objects.get(id=item.product_id)
                product.amount -= item.quantity
                product.save()
               
                #************ <> *****************

            ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items']=0
            messages.success(request, "Your Order has been completed. Thank you ")
            context={'ordercode':ordercode,'category': category}
            return render(request, 'cart/order_completed.html',context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse("cart:orderproduct"))

    form= OrderForm()
    profile = Customer.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'cart/order_form.html', context)