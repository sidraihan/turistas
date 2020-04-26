from django.urls import path
from . import views

from turistas_rec.views import ClubChartView

urlpatterns = [
    #path('', views.index, name='index'),
    #path('places/', views.ListPlacesView.as_view(), name="places-all")
    path('',ClubChartView.as_view(),name='home'),
    #path('pie-chart/', views.pie_chart, name='pie-chart'),
    #path('population-chart/', views.population_chart, name='population-chart'),

]