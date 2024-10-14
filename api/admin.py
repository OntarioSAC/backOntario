from dal import autocomplete
from django import forms
from django.contrib import admin
from .models import CronogramaPagos, Cuota, CuotaInicialFraccionada, DetallePersona, Empresa, FichaDatosCliente, Lote, ObservacionSeparacion, Observaciones, PersonaClient, PersonaClient, PersonaStaff, Proyecto, SeparacionCliente


# admin.site.register(Lote)
admin.site.register(Cuota)
admin.site.register(Empresa)
admin.site.register(Proyecto)
admin.site.register(PersonaStaff)
admin.site.register(PersonaClient)
admin.site.register(Observaciones)
admin.site.register(DetallePersona)
admin.site.register(CronogramaPagos)
# admin.site.register(FichaDatosCliente)
admin.site.register(CuotaInicialFraccionada)

admin.site.register(SeparacionCliente)
admin.site.register(ObservacionSeparacion)



class FichaDatosClienteForm(forms.ModelForm):
    class Meta:
        model = FichaDatosCliente
        fields = '__all__'
        widgets = {
            # 'id_persona': autocomplete.ModelSelect2(url='persona-autocomplete'),
            'id_lote': autocomplete.ModelSelect2(url='lote-autocomplete'),
            'id_cpagos': autocomplete.ModelSelect2(url='cpagos-autocomplete'),
        }

class FichaDatosClienteAdmin(admin.ModelAdmin):
    form = FichaDatosClienteForm
    list_display = ('id_fichadc', 'estado_legal', 'id_lote', 'id_cpagos')
    # antes:    list_display = ('id_fichadc', 'estado_legal', 'id_persona', 'id_lote', 'id_cpagos')

# Registrar FichaDatosCliente con FichaDatosClienteAdmin
admin.site.register(FichaDatosCliente, FichaDatosClienteAdmin)


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    search_fields = ['manzana_lote', 'id_proyecto__nombre_proyecto']  # Campos para buscar

    list_display = ['id_lote', 'manzana_lote', 'area', 'estado', 'id_proyecto']