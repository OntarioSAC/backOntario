from django.contrib import admin
from django import forms
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Persona, PersonaProyecto, Proyecto, Rol

class PersonaProyectoForm(forms.ModelForm):
    class Meta:
        model = PersonaProyecto
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PersonaProyectoForm, self).__init__(*args, **kwargs)
        if 'id_proyecto' in self.data:
            try:
                id_proyecto = int(self.data.get('id_proyecto'))
                self.fields['id_manzana'].queryset = Manzana.objects.filter(id_proyecto=id_proyecto).order_by('nombre_manzana')
            except (ValueError, TypeError):
                self.fields['id_manzana'].queryset = Manzana.objects.none()
        elif self.instance.pk:
            self.fields['id_manzana'].queryset = self.instance.id_proyecto.manzana_set.order_by('nombre_manzana')

# Administrador personalizado para el modelo PersonaProyecto
class PersonaProyectoAdmin(admin.ModelAdmin):
    form = PersonaProyectoForm


admin.site.register(Proyecto)
admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(Lote)
admin.site.register(Estado)
admin.site.register(Manzana)
admin.site.register(PersonaProyecto, PersonaProyectoAdmin)
admin.site.register(Area)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Origen)
admin.site.register(Observaciones)




