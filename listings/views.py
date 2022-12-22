from django.shortcuts import render
from .models import Categories,Properties,Places

# Create your views here.

def Home(request):
    categories = Categories.objects.all()
    properties = Properties.objects.all()
    places = Places.objects.all()
    context={"categories":categories,"properties":properties,"places":places}
    return render(request,'listings/home.html',context)

def PlacesToVIsit(request,pk):
    place = Places.objects.get(slug=pk)    
    context={"place":place}
    return render(request,'listings/places.html',context)