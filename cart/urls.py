from django.urls import path
from . import views
app_name= "cart"
urlpatterns = [
   
    path('checkout/', views.checkout,name="checkout"),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    
]