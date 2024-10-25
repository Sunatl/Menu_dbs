
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Menu

def home(request):
    menu = Menu.objects.all()
    return render(request,'main.html',context={"menu": menu})

def name(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

