from django.shortcuts import render
from .models import *

def main(request):
    traffics = Streets.objects.all()
    if request.method == 'POST':
        traffics = Streets.objects.all().filter(name=request)
    return render(request, 'mapp/main.html', {'traffics': traffics})

def search(request):
    logs = Log.objects.all()
    if request.method == 'POST':
        quest = request.POST.get('quest')
        logs = Log.objects.filter(actor=quest)
    return render(request, 'mapp/search.html', {'logs': logs})

def map(request):
    streets = Streets.objects.all()
    return render(request, 'mapp/map.html', {'streets': streets})