from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path(route="register/",view=views.user_register,name="user_register")
]