from django.contrib import admin
from django import forms
from .models import CronogramaPagos, Cuota, Lote, Observaciones, Persona, FichaDatosCliente, Proyecto



admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Lote)
admin.site.register(FichaDatosCliente)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Observaciones)
