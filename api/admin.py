from django.contrib import admin

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
admin.site.register(Rol)
admin.site.register(Lote)
admin.site.register(Estado)
admin.site.register(Manzana)
admin.site.register(PersonaProyecto)
admin.site.register(Area, AreaAdmin)
admin.site.register(PermisoArea)
admin.site.register(Permiso)
admin.site.register(ClienteCerrado)
admin.site.register(CronogramaPagos)
admin.site.register(Cuota)
admin.site.register(Medio)
admin.site.register(Canal)
admin.site.register(Origen)
admin.site.register(Observaciones)





#admin.site.register(CronogramaPagos)