from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .serializers import PlaceSerializer
from rest_framework import generics
import firebase
from firebase.firebase import FirebaseApplication
from django.core import serializers



''' class ListPlacesView(generics.ListAPIView):

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the turista's index.") '''

app = FirebaseApplication('https://djangoplaces.firebaseio.com/', None)  
qs = Place.objects.all()


data_dict = []
for a in qs:
    data_dict.append(a.name)
    #qs_json = serializers.serialize('json', data_dict)
    result = app.post('/djangoplaces/Places',data_dict)  
    print(result.name)




'''result = app.post('/djangoplaces/Places',qs_json)  
print(result)
 ''' 
