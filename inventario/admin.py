from django.contrib import admin
import adminactions.actions as actions

# Register your models here.
from .models import PC, Area, Region, RAM, Cpu, Monitor, Tarjeta_de_Red, Lector, Fuente_Interna, Estabilizador, UPS, \
    Bocinas, Mouse, Teclado, HDD, Motherboard, Tarjeta_de_Video, SO, Impresora, TipoCapacidadHDD, TipoCapacidadCPU


class CpuInline(admin.StackedInline):
    model = Cpu
    extra = 0


class RamInline(admin.StackedInline):
    model = RAM
    extra = 0


class MonitorInline(admin.StackedInline):
    model = Monitor
    extra = 0


class Targeta_de_Red_Inline(admin.StackedInline):
    model = Tarjeta_de_Red
    extra = 0


class Targeta_de_Video_Inline(admin.StackedInline):
    model = Tarjeta_de_Video
    extra = 0


class Lector_Inline(admin.StackedInline):
    model = Lector
    extra = 0


class Fuente_Intera_Inline(admin.StackedInline):
    model = Fuente_Interna
    extra = 0


class EstabilizadorInline(admin.StackedInline):
    model = Estabilizador
    extra = 0


class Ups_Inline(admin.StackedInline):
    model = UPS
    extra = 0


class Bocinas_Inline(admin.StackedInline):
    model = Bocinas
    extra = 0


class Mouse_Inline(admin.StackedInline):
    model = Mouse
    extra = 0


class Teclado_Inline(admin.StackedInline):
    model = Teclado
    extra = 0


class HDD_Inline(admin.StackedInline):
    model = HDD
    extra = 0


class Motherboard_Inline(admin.StackedInline):
    model = Motherboard
    extra = 0


class Impresora_Inline(admin.StackedInline):
    model = Impresora
    extra = 0


class PcAdmin(admin.ModelAdmin):
    inlines = [CpuInline, RamInline, MonitorInline, Targeta_de_Red_Inline, Targeta_de_Video_Inline, Lector_Inline,
               Fuente_Intera_Inline, EstabilizadorInline, Ups_Inline, Bocinas_Inline, Mouse_Inline, Teclado_Inline, HDD_Inline, Motherboard_Inline, Impresora_Inline]


admin.site.register(PC, PcAdmin)
admin.site.register(Area)
admin.site.register(Region)
admin.site.register(RAM)
admin.site.register(Cpu)
admin.site.register(Tarjeta_de_Red)
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
admin.site.register(Tarjeta_de_Video)
admin.site.register(SO)
admin.site.register(Impresora)
admin.site.register(TipoCapacidadHDD)
admin.site.register(TipoCapacidadCPU)
actions.add_to_site(admin.site)
