from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Homepage")


def home(request):

    restaurants = Restaurant.objects.all()
    print(restaurants)
    return render(request, "index.html", {'items': restaurants})


def pfc(request):

    restaurants = Restaurant.objects.all()
    print(restaurants)
    return render(request, "pfc.html", {'items': restaurants})


def restaurant(request, resto):
    print(resto)
    fooditems = Food.objects.filter(restaurant__contains=resto)
    restaurant = Restaurant.objects.get(tag=resto)
    print(fooditems, restaurant)
    return render(request, "resto.html", {'menu': fooditems, 'restaurant': restaurant})


# def about(request):

#     backimg = BackgroundNav.objects.all()
#     aboutitems = About.objects.all()
#     # return response with template and context
#     return render(request, "about.html", {'items': aboutitems, 'background': backimg})


def contact(request):

    # return response with template and context
    return render(request, "contact.html")
