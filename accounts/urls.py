from django.urls import path
from . import views
from django.contrib.auth import views as authViews

app_name= "accounts"
urlpatterns = [
   
    path('register/', views.register,name="register"),
    path('login/', views.userLogin,name="login"),
    path('logout/', views.userLogout,name="logout"),
    path('password/', views.password_change, name='password_change'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.user_update, name='user_update'),
    path('user_order/', views.user_order, name='user_order'),
    path('user_comment/', views.user_comment, name='user_comment'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
    path('user_order_detail/<int:id>', views.user_orderdetail, name='user_order_detail'),
    path('orders_product/', views.user_order_product, name='user_order_product'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),
    #************Forgot password***************************
    path('reset_password/', authViews.PasswordResetView.as_view(
        template_name="auth/password_reset.html"), name="reset_password"),
     path('reset_password_sent/', authViews.PasswordResetDoneView.as_view(
         template_name="auth/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(
        template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(
        template_name="auth/password_reset_done.html"), name="password_reset_complete"),
        #************************************************************#
    
   
    
]