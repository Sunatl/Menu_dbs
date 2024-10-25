from django.urls import path
from .views import home,name

urlpatterns = [
    path("Online_menu",home),
    path("Menu",name)
    
]