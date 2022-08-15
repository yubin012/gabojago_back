from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.
def maps(request):
    return render(request, 'maps.html')

def map(requset):
    return render(requset,'map.html')
