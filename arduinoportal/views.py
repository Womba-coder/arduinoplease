from re import template
from django.shortcuts import render
from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer
from django.views.generic import ListView

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
class CreateView(generics.CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
class InfoListView(ListView):
    model = Info
    template_name = 'list.html'
