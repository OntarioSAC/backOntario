from django.contrib import admin
from django import forms
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Persona, FichaDatosCliente, Proyecto, Rol

class FichaDatosClienteForm(forms.ModelForm):
    class Meta:
        model = FichaDatosCliente
        fields = '__all__'
        
    class Media:
        js = ('js/filter_manzanas.js', 'js/filter_lotes.js')  # Incluye ambos archivos JavaScript
    
    def __init__(self, *args, **kwargs):
        super(FichaDatosClienteForm, self).__init__(*args, **kwargs)
        if 'id_proyecto' in self.data:
            try:
                id_proyecto = int(self.data.get('id_proyecto'))
                self.fields['id_manzana'].queryset = Manzana.objects.filter(id_proyecto=id_proyecto).order_by('nombre_manzana')
            except (ValueError, TypeError):
                self.fields['id_manzana'].queryset = Manzana.objects.none()
        elif self.instance.pk:
            self.fields['id_manzana'].queryset = self.instance.id_proyecto.manzana_set.order_by('nombre_manzana')
        
        if 'id_manzana' in self.data:
            try:
                id_manzana = int(self.data.get('id_manzana'))
                self.fields['id_lote'].queryset = Lote.objects.filter(id_manzana=id_manzana).order_by('numero_lote')
            except (ValueError, TypeError):
                self.fields['id_lote'].queryset = Lote.objects.none()
        elif self.instance.pk:
            self.fields['id_lote'].queryset = self.instance.id_manzana.lote_set.order_by('numero_lote')

        # Asignar solo una vez un cronograma de pagos
        if self.instance and self.instance.pk:
            # Incluye solo el id_cpagos actual y los no asignados
            self.fields['id_cpagos'].queryset = CronogramaPagos.objects.filter(fichadatoscliente__isnull=True) | CronogramaPagos.objects.filter(id_cpagos=self.instance.id_cpagos_id)
        else:
            # Excluir todos los id_cpagos que ya están asignados
            self.fields['id_cpagos'].queryset = CronogramaPagos.objects.filter(fichadatoscliente__isnull=True)
        
class FichaDatosClienteAdmin(admin.ModelAdmin):
    form = FichaDatosClienteForm

admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(Lote)
admin.site.register(Estado)
admin.site.register(Manzana)
admin.site.register(FichaDatosCliente, FichaDatosClienteAdmin)
admin.site.register(Area)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Origen)
admin.site.register(Observaciones)
