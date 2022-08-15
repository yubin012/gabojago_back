from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.
def maps(request):
    return render(request, 'maps.html')

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Place.objects.all()
    serializer = PlaceSerializer(randomQuizs, many=True) #many 부분을 통해 다량의 데이터도 직렬화 진행
    return Response(serializer.data)