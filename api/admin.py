from dal import autocomplete
from django import forms
from django.contrib import admin
from .models import CronogramaPagos, Cuota, CuotaInicialFraccionada, DetallePersona, Empresa, FichaDatosCliente, Lote, Observaciones, PersonaClient, PersonaClient, PersonaStaff, Proyecto


admin.site.register(Lote)
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