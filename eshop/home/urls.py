from django.urls import path
from . import views

app_name="home"

urlpatterns=[
    path(route="django/home/",view=views.home,name="home"),
     path(route="django/about/",view=views.about,name="about")
]