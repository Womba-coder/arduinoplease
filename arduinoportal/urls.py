from xml.etree.ElementInclude import include
from django.urls import path
from .views import ListView,CreateView,InfoListView


urlpatterns = [
    path('',ListView.as_view()),
    path('post',CreateView.as_view()),
    path('',InfoListView.as_view(),name='home')
]