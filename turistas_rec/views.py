from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .serializers import PlaceSerializer
from rest_framework import generics


class ListPlacesView(generics.ListAPIView):

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the turista's index.")