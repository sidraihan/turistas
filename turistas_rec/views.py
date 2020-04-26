from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Review
from .serializers import PlaceSerializer
from rest_framework import generics
import firebase
from firebase.firebase import FirebaseApplication
from django.core import serializers
# Import database module.
from firebase_admin import db
from django.views.generic import TemplateView

# Get a database reference to our blog.



''' class ListPlacesView(generics.ListAPIView):

    queryset = Place.objects.all()[0:3]
    serializer_class = PlaceSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the turista's index.") '''
'''
app = FirebaseApplication('https://djangoplaces.firebaseio.com/', None)  
qs = Place.objects.all()
rev = Review.objects.all()
rev_text = ""
data_dict = {}
rev_data = {}
for a in qs: 
    data_dict.update({"name":a.name,"specification":a.specification.name,"description":a.description,"latitude":a.latitude,"longitude":a.longitude,"howtoreach":a.howtoreach,"ratings":a.ratings,"visited":a.visited,"view":a.view})
    result = app.post('/Places',data_dict)  

for r in rev:
    rev_data.update({"name":r.place_ref.name,"rev_text":r.review_text,"specification":r.place_ref.specification.name,"ratings":r.place_ref.ratings})
    result2 = app.post('/Review',rev_data)
    '''
'''result = app.post('/djangoplaces/Places',qs_json)  
print(result)
 ''' 
class ClubChartView(TemplateView):
    template_name = 'charts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"]= Place.objects.all()
        return context

'''def pie_chart(request):
    labels = []
    data = []

    queryset = Place.objects.order_by('-ratings')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.ratings)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })
def home(request):
    return render(request, 'home.html')


def population_chart(request):
    labels = []
    data = []

    queryset = Place.objects.values('ratings').annotate(place_ratings=Sum('ratings')).order_by('-ratings')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    '''
