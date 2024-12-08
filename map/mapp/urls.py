from . import views
from django.urls import path

urlpatterns = [
    path('request/', views.requ, name='requ'),
    path('', views.map, name='map'),
]
