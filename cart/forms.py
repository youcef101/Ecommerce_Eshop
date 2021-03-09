from django.forms import ModelForm
from .models import ShopCart,Order

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','address','phone','city','country']

