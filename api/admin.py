from django.contrib import admin
<<<<<<< HEAD
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
=======

from api.serializer import AreaSerializer
from .models import Area, Canal, ClienteCerrado, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Permiso, PermisoArea, Persona, PersonaProyecto, Programmer, Proyecto, Rol

# Register your models here.

class PersonaProyectoInline(admin.TabularInline):
    model = PersonaProyecto
    extra = 1

class PersonaAdmin(admin.ModelAdmin):
    inlines = [PersonaProyectoInline]
    list_display = (
        'nombres_apellidos',
        'celular',
        'dni',
        'correo',
        'conyuge',
        'direccion',
        'id_rol',
        'id_area'
    )
   
    # search_fields = ('nombres_apellidos',)
    # list_filter = ('dni','nombre_proyecto')
    # filter_horizontal = ['nombre_proyecto',] 
    

class PermisoAreaInline(admin.TabularInline):
    model = PermisoArea
    extra = 1

class AreaAdmin(admin.ModelAdmin):
    inlines = [PermisoAreaInline]
    list_display = (
        'nombre_area',
        'descripcion_area',
    )
    




# admin.site.register(Programmer)
admin.site.register(Proyecto)
admin.site.register(Persona, PersonaAdmin)
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
admin.site.register(Rol)
admin.site.register(Lote)
admin.site.register(Estado)
admin.site.register(Manzana)
<<<<<<< HEAD
admin.site.register(PersonaProyecto, PersonaProyectoAdmin)
admin.site.register(Area)
=======
admin.site.register(PersonaProyecto)
admin.site.register(Area, AreaAdmin)
admin.site.register(PermisoArea)
admin.site.register(Permiso)
admin.site.register(ClienteCerrado)
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Origen)
admin.site.register(Observaciones)




<<<<<<< HEAD
=======

#admin.site.register(CronogramaPagos)
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
