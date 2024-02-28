from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import GenreModel, CrimeModel, SuspectModel, VictimModel
from django.urls import reverse_lazy

# Create your views here.
class GenreList(ListView):
    model = GenreModel
    template_name = 'genre_list.html'

class CrimeList(ListView):
    model = CrimeModel
    template_name = 'crime_list.html'

class CrimeDetail(DetailView):
    model = CrimeModel
    template_name = 'crime_detail.html'

class CrimeCreate(CreateView):
    model = CrimeModel
    fields = ['crime_name', 'crime_name_second', 'crime_start_datetime', 'crime_end_datetime', 'crime_place', 'crime_fact']
    template_name = 'crime_create.html'
    success_url = reverse_lazy('crime')

class SuspectDetail(DetailView):
    model = SuspectModel
    template_name = 'suspect_detail.html'

class VictimDetail(DetailView):
    model = VictimModel
    template_name = 'victim_detail.html'
