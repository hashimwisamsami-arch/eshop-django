from django.urls import path
from . import views

app_name="accounts"

urlpatterns=[
    path(route="register/",view=views.user_register,name="user_register"),
    path(route="login/",view=views.user_login,name="user_login"),
    path(route="logout/",view=views.user_logout,name="user_logout"),
    path(route="profile/",view=views.user_profile,name="user_profile"),
]