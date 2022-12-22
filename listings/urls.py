from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
        path('places/<str:pk>/',views.PlacesToVIsit,name='places-to-visit'),
]