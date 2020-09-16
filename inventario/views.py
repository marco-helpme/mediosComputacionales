from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import PC, Area, Region

def index(request):
    region = Region.objects.all()
    area = Area.objects.all()
    context = {'area': area, 'region': region}
    return render(request, 'inventario/index.html', context)

def detail(request, id):
    area = Area.objects.get(id=id)
    pc = PC.objects.all()
    context = {'area': area, 'pc': pc}
    return render(request, 'inventario/detail.html', context)