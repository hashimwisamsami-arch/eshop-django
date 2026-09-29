
from django.shortcuts import render, redirect
from .forms import RgisterForm
from django.contrib.auth.models import User


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

