from django.urls import path
from . import views

urlpatterns = [
    path('findfood/', views.findfood, name='Randomizer'),
    path('findfood_old', views.findfood_old, name='Randomizer'),
    path('ping/', views.ping_request, name='ping')
]
