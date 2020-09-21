from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import PC, Area, Region, Impresora, Cpu, RAM, Bocinas, Estabilizador, Fuente_Interna, HDD, Lector, Monitor, \
    Motherboard, Mouse, SO, Targeta_de_Red, Targeta_de_Video, Teclado, UPS


def index(request):
    region = Region.objects.all()
    area = Area.objects.all()
    pc = PC.objects.all()
    impresora = Impresora.objects.all()
    cantidadpc = PC.objects.count()
    cantidadImpresora = Impresora.objects.count()
    PcRed = PC.objects.filter(enRed=True).count()

    context = {'area': area, 'region': region, 'pc': pc, 'cantidadpc': cantidadpc,
               'cantidadImpresora': cantidadImpresora, 'PcRed': PcRed}
    return render(request, 'inventario/index.html', context)


def detail(request, id):
    area = Area.objects.get(id=id)
    pc = PC.objects.all()
    cantidadpc = PC.objects.filter(area_id=id).count()
    cantidadImpresora = Impresora.objects.filter(pc__area_id=id).count()
    PcRed = PC.objects.filter(area_id=id).filter(enRed=True).count()
    context = {'area': area, 'pc': pc, 'cantidadpc': cantidadpc, 'cantidadImpresora': cantidadImpresora, 'PcRed': PcRed}

    return render(request, 'inventario/detail.html', context)


def region_detail(request, id):
    area = Area.objects.get(id=id)
    pc = PC.objects.all()
    cantidadpc = PC.objects.filter(area__region_id=id).count()
    cantidadImpresora = Impresora.objects.filter(pc__area__region_id=id).count()
    PcRed = PC.objects.filter(area__region_id=id).filter(enRed=True).count()
    context = {'area': area, 'pc': pc, 'cantidadpc': cantidadpc, 'cantidadImpresora': cantidadImpresora, 'PcRed': PcRed}

    return render(request, 'inventario/detail.html', context)


def area_detail(request, id):
    area = Area.objects.get(id=id)
    pc = PC.objects.filter(area__id=id)
    cantidadpc = PC.objects.filter(area__id=id).count()
    cantidadImpresora = Impresora.objects.filter(pc__area__id=id).count()
    PcRed = PC.objects.filter(area__id=id).filter(enRed=True).count()
    context = {'area': area, 'pc': pc, 'cantidadpc': cantidadpc, 'cantidadImpresora': cantidadImpresora, 'PcRed': PcRed}

    return render(request, 'inventario/detail.html', context)


def pc_component(request, id):
    pc = PC.objects.get(id=id)
    # try:
    #     impresora = Impresora.objects.get(pc_id=id)
    #
    try:
        impresora = Impresora.objects.get(pc_id=id)
        cpu = Cpu.objects.filter(pc_id=id)
        ram = RAM.objects.filter(pc_id=id)
        motherboard = Motherboard.objects.filter(pc_id=id)
        ups = UPS.objects.filter(pc_id=id)
        trajeta_de_video = Targeta_de_Video.objects.filter(pc_id=id)
        tarjeta_de_red = Targeta_de_Red.objects.filter(pc_id=id)
        monitor = Monitor.objects.filter(pc_id=id)
        mouse = Mouse.objects.filter(pc_id=id)
        teclado = Teclado.objects.filter(pc_id=id)
    except:
        impresora = ''
        cpu = ''
        ram = ''
        motherboard = ''
        ups = ''
        trajeta_de_video = ''
        tarjeta_de_red = ''
        monitor = ''
        mouse = ''
        teclado = ''

    context = {'pc': pc, 'impresora': impresora, 'cpu': cpu, 'ram': ram, 'motherboard': motherboard, 'ups': ups,
               'trajeta_de_video': trajeta_de_video, 'tarjeta_de_red': tarjeta_de_red, 'monitor': monitor,
               'mouse': mouse, 'teclado': teclado}
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
    areas = Area.objects.all()

    context = {'region': region, 'areas': areas}
    return context
