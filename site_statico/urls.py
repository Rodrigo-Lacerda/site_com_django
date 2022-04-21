from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
]
