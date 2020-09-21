from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import PC, Area, Region, Impresora, Cpu, RAM, Bocinas


def index(request):
    region = Region.objects.all()
    area = Area.objects.all()
    pc = PC.objects.all()
    impresora = Impresora.objects.all()
    cantidadpc = []
    for a in area:
        cantidadpc.append(cantpc(
            pc, a, impresora
        ))

    context = {'area': area, 'region': region, 'pc': pc, 'cantidadpc': cantidadpc}
    return render(request, 'inventario/index.html', context)


def detail(request, id):
    area = Area.objects.get(id=id)
    pc = PC.objects.all()
    context = {'area': area, 'pc': pc}
    return render(request, 'inventario/detail.html', context)


def pc_component(request, id):
    pc = PC.objects.get(id=id)
    # try:
    #     impresora = Impresora.objects.get(pc_id=id)
    #
    try:
        impresora = Impresora.objects.get(pc_id=id)
    except:
        impresora = ''
    try:
        cpu = Cpu.objects.filter(pc_id=id)
    except:
        cpu = 'no tiene o tiene mas de uno'

    ram = RAM.objects.filter(pc_id=id)


    context = {'pc': pc, 'impresora': impresora, 'cpu': cpu, 'ram': ram}
    return render(request, 'inventario/pc_component.html', context)


def cantpc(pc, area, impresoras):
    cantpc = 0
    enred = 0
    cantidadImpresoras = 0
    for pc in pc:
        if pc.area.id == area.id:
            cantpc = cantpc + 1
            if pc.enRed:
                enred = enred + 1
            for impresora in impresoras:
                if impresora.pc.id == pc.id:
                    cantidadImpresoras = cantidadImpresoras + 1
    payload = {'area': area, 'cantpc': cantpc, 'enred': enred, 'cantImpresoras': cantidadImpresoras}
    return payload

def bocinasList(request):
    bocinas = Bocinas.objects.all()


    context = {'bocinas': bocinas}
    return render(request, 'inventario/bocinas/bocinaslist.html', context)

# def layout(request):
#     region = Region.objects.all()
#
#     context = {'region': region}
#     return render(request, 'layout.html', context)

def region_context_processors(HttpRequest):
    region = Region.objects.all()

    context = {'region': region}
    return context