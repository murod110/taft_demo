from django.urls import path
from .views import *


urlpatterns = [
    path('',Home,name='home'),
    path('/printed/<id>/',homHotel,name='hh'),
    path('best/',Best,name='best'),
    path('category/',Categorys,name='category'),
    path('category/palet/<id>/',designs,name="designs"),
    path('news/',Saling,name="news"),
    path('product/more/<carpet_id>/',More,name="more"),
    path("search",Search,name="search"),
    
    path("product/cart",Cart,name="cart"),
    path("product/buying/<id>/",Buy,name="buy"),
    path("product/card/purchase",Purchase,name="purchase"),
    path('category/home/<id>/',categoryHome,name="cat-home"),
    path('printed/<type>',Printed_Carpets,name="print-cat"),
    path("product/buy/remove/<id>",Remove,name="remove"),
    path("product/buying/cart/clear",Clear_Order,name="clear"),
    path("user/sign_up", signup, name="sign"),
    path("user/logout",logout_user,name="logout"),
    # For Users
    path('login',userLogin,name="login"),
    path('signup',userSignup,name="signup")
    
]
