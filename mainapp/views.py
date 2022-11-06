from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Homepage")


def home(request):

    restaurants = Restaurant.objects.all()
    return render(request, "index.html", {'eateries': restaurants})


# def about(request):

#     backimg = BackgroundNav.objects.all()
#     aboutitems = About.objects.all()
#     # return response with template and context
#     return render(request, "about.html", {'items': aboutitems, 'background': backimg})


def contact(request):

    # return response with template and context
    return render(request, "contact.html")
