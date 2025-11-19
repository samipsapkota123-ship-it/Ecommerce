from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login ,logout
from .forms import LoginForm
from django.contrib import messages


# Create your views here.

def register_user(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,' Succesfully Registered')
            return redirect('login')
        else:
            return render(request,"accounts/user_register.html",{  'form':UserCreationForm 
                                                                 })
    return render(request,"accounts/user_register.html",{  'form':UserCreationForm })

def login_user(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            username=data["username"]
            password=data["password"]
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
              
                return redirect('product')
            else:
                messages.add_message(request,messages.ERROR,' User not found')
                return redirect('register')
        else:
            return render(request,"accounts/login.html",{'form':form})

    
    return render(request,"accounts/login.html",{'form':LoginForm()})

def logout_user(request):
    logout(request)
    return redirect('homepage')