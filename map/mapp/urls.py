from . import views
from django.urls import path

urlpatterns = [
    path('request/', views.requ, name='requ'),
    path('analitics/', views.analitics, name='analitic'),
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
]
