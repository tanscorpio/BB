from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})
def signin(request):
    if request.method == "POST":
        un=request.POST['username']
        p1=request.POST['pass1']
        arg={}
        user = authenticate(username=un, password=p1)
        if user is not None:
            login(request, user)
            return redirect('sell')  
        else:
            arg={ 'err':True }
            return render(request, 'home/signin.html', arg )
    else:
        return render(request, 'home/signin.html', {})
def signup(request):
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        arg={}
        if  not User.objects.filter(username=username).exists():
            User.objects.create_user(first_name=name,username=username,password=pass1)
            return redirect('/signin')
        else:
            arg={ 'err':True }
            return render(request, 'home/signup.html', arg  )          

    else:
        return render(request, 'home/signup.html', {})