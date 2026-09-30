
from django.shortcuts import render, redirect
from .forms import RgisterForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def user_register(request):
    if request.method == "POST":
        form = RgisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            User.objects.create_user(
                username=data["user_name"],
                email=data["email"],
                password=data["confirm_password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )

            return redirect("home:home")

    else:
        form = RgisterForm()

    context = {"form": form}

    return render(request, "accounts/register.html", context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            try:
                user=authenticate(
                               request,
                               username=User.objects.get(email=data['user']),
                               password=data['password'])
            except:
                 user=authenticate(
                                request,
                                username=data['user'],
                                password=data['password'])
           
            if user is not None:
                login(request,user)
                return redirect("home:home")
          
            else:
                print("wrong username or password")

    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("home:home")