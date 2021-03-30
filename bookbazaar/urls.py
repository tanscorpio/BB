from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sell', views.sell , name='sell'),
    path('logot', views.lout , name='logot'),
    path('buy', views.buy , name='buy'),
    path('myorders', views.myorders , name='myorders'),
    path('cart', views.cart , name='cart'),
    path('checkout', views.checkout , name='checkout'),
    path('atc/<int:pid>', views.atc , name='atc'),
    path('rmc/<int:pid>', views.rmc , name='rmc'),
    path('vieworder/<int:pid>', views.vieworder , name='vieworder'),
    
]