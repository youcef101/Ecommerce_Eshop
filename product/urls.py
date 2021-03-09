from django.urls import path
from . import views
app_name= "product"
urlpatterns = [
   
    path('product_detail/', views.detail,name="product_detail"),
    path('product_list/', views.product,name="product_list"),
    path('addcomment/<int:id>', views.addcomment,name="addcomment"),
   
    
]