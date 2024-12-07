from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.map, name='map'),
]
