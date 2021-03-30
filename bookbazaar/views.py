from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


def lout(request):
    logout(request)
    return redirect("/")

def sell(request): 
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context={}
        if request.method == "GET":
            return render(request,'bookbazaar/sell.html',{})
        else:
            name=request.POST['bookname']
            author=request.POST['author']
            price=request.POST['price']
            product = Product(name=name, author=author ,price=price)
            product.save()
            user=request.user
            sellitem=SellItem(user=user,product=product)
            sellitem.save()
            context={'arg': True }
            return render(request,'bookbazaar/sell.html',context)
    

@login_required(login_url='/')
def buy(request):
    products=Product.objects.all()
    context={ 'products':products }  
    return render(request,'bookbazaar/buy.html',context)

def myorders(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    sellitem=SellItem.objects.filter(user=user)
    context={ 'products':orders, 'productsb':sellitem }
    return render(request,'bookbazaar/myorders.html',context)

def cart(request):
    user=request.user
    orderitem=OrderItem.objects.filter(user=user,ordered=False)
    total=0
    for oi in orderitem:
        total+=oi.product.price
    context={ 'products':orderitem, 'total':total }
    return render(request,'bookbazaar/cart.html',context)

def checkout(request):
    user=request.user
    orderitems=OrderItem.objects.filter(user=user,ordered=False)
    order=Order(user=user,total=0)
    order.save()
    for oi in orderitems:
        oi.ordered=True
        oi.save()
        order.orderitem.add(oi)
        order.total+=oi.product.price
        order.save()  
    orderitem=order.orderitem.all()
    context={ 'products':orderitem , 'order':order }
    return render(request,'bookbazaar/checkout.html',context)

def vieworder(request,pid):
    order=Order.objects.get(pk=pid)
    orderitem=order.orderitem.all()
    context={ 'products':orderitem , 'order':order }
    return render(request,'bookbazaar/vieworder.html',context)



def atc(request,pid):
    product=Product.objects.get(pk=pid)
    user=request.user
    orderitem=OrderItem(user=user,ordered=False,product=product)
    orderitem.save()
    return redirect("buy")

def rmc(request,pid):
    orderitem=OrderItem.objects.get(pk=pid)
    orderitem.delete()
    return redirect("cart")
