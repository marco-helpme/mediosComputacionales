from django.contrib import admin

# Register your models here.
from .models import PC, Area, Region, RAM, Cpu, Monitor, Targeta_de_Red, Lector, Fuente_Interna, Estabilizador, UPS, \
    Bocinas, Mouse, Teclado, HDD, Motherboard, Targeta_de_Video, SO, Impresora

admin.site.register(PC)
admin.site.register(Area)
admin.site.register(Region)
admin.site.register(RAM)
admin.site.register(Cpu)
admin.site.register(Targeta_de_Red)
admin.site.register(Lector)
admin.site.register(Fuente_Interna)
admin.site.register(Monitor)
admin.site.register(Estabilizador)
admin.site.register(UPS)
admin.site.register(Bocinas)
admin.site.register(Mouse)
admin.site.register(Teclado)
admin.site.register(HDD)
admin.site.register(Motherboard)
admin.site.register(Targeta_de_Video)
admin.site.register(SO)
admin.site.register(Impresora)
