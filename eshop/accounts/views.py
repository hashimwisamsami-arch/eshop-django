
from django.shortcuts import render, redirect
from .forms import RgisterForm,LoginForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile


def user_register(request):
    if request.user.is_authenticated:
        return redirect("home:home")
    if request.method == "POST":
        form = RgisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_user=User.objects.create_user(
                username=data["user_name"],
                email=data["email"],
                password=data["confirm_password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            new_user.save()

            return redirect("home:home")

    else:
        form = RgisterForm()

    context = {"form": form}

    return render(request, "accounts/register.html", context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home:home")
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
                messages.success(request,message="logged in successfully",extra_tags="success")
                return redirect("home:home")
          
            else:
                messages.error(request,message="invalid username or password",extra_tags="danger")

    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    messages.success(request,message="logged out successfully",extra_tags="success")
    return redirect("home:home")

def user_profile(request):
    profile=Profile.objects.get(user_id=request.user.id)
    context={'profile':profile}
    return render(request, "accounts/profile.html",context)

def user_update(request):
    if request.method=="POST":
        user_update_form=UserUpdateForm(request.POST,instance=request.user)
        profile_update_form=ProfileUpdateForm(request.POST,instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request,"updated successfully","success")
            return redirect("accounts:user_profile")
    else:
        user_update_form=UserUpdateForm(instance=request.user)
        profile_update_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_update_form':user_update_form,
        'profile_update_form':profile_update_form
        }
    return render(request, "accounts/update.html",context)