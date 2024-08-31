from django.contrib import admin
from django import forms
from .models import Area, Canal, CronogramaPagos, Cuota, Documento, Lote, Medio, Observaciones, Origen, Persona, FichaDatosCliente, Proyecto, Rol, Usuario



admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(Lote)
admin.site.register(FichaDatosCliente)
admin.site.register(Area)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Origen)
admin.site.register(Observaciones)
admin.site.register(Usuario)
admin.site.register(Documento)
