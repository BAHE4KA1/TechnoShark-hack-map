from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.search, name='search'),
    path('map/', views.map, name='map'),
]
