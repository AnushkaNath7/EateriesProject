
from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.home),
    # path('about', views.about),

    path('contact', views.contact),

]
