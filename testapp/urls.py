from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.home, name="home"),
    path("index",views.index, name="index"),
    path("register",views.register, name="register"),
    path("randomGenerate",views.randomGenerate, name="randomGenerate")
    
]
