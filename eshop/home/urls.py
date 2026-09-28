from django.urls import path
from . import views

app_name="home"

urlpatterns=[
    path(route="home/",view=views.home,name="home"),
     path(route="about/",view=views.about,name="about")
]