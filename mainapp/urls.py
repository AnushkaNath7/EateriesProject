
from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.home),
    # path('pfc', views.pfc),
    path('restaurants/<str:resto>', views.restaurant),

    path('contact', views.contact),

]
