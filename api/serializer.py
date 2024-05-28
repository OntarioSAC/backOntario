<<<<<<< HEAD
from rest_framework import serializers
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Persona, PersonaProyecto, Rol, Proyecto

# Serializer del modelo Area
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            'id_area',
            'nombre_area',
            'descripcion_area'
        ]

# Serializer del modelo Rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = [
            'id_rol',
            'nombre_rol'
        ]

# Serializer del modelo Persona
class PersonaSerializer(serializers.ModelSerializer):
    id_rol = RolSerializer()
    id_area = AreaSerializer()
    
    class Meta:
        model = Persona
        fields = [
            'id_persona',
            'nombres_apellidos',
            'celular',
            'dni',
            'correo',
            'conyuge',
            'direccion',
            'fecha_registro',
            'profesion',
            'ocupacion',
            'centro_trabajo',
            'direccion_laboral',
            'antiguedad_laboral',
            'constancia_inicial',
            'id_rol',
            'id_area',
            'id_origen',
            'id_canal',
            'id_medio'
        ]




# Serializer del modelo Estado
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = [
            'id_estado',
            'nombre_estado'
        ]

# Serializer del modelo Lote


class LoteSerializer(serializers.ModelSerializer):
    id_estado = EstadoSerializer()

    class Meta:
        model = Lote
        fields = [
            'id_lote',
            'numero_lote',
            'area',
            'perimetro',
            'colindancia_frente',
            'colindancia_derecha',
            'colindancia_izquierda',
            'colindancia_fondo',
            'distancia_frente',
            'distancia_derecha',
            'distancia_izquierda',
            'distancia_fondo',
            'precio_m2',
            'id_estado'
        ]


# Serializer del modelo Manzana
class ManzanaSerializer(serializers.ModelSerializer):
    id_lote = LoteSerializer(many=True, source='lote_set')

    class Meta:
        model = Manzana
        fields = [
            'id_manzana',
            'nombre_manzana',
            'id_lote'
        ]


# Serializer del modelo Proyecto
class ProyectoSerializer(serializers.ModelSerializer):
    id_manzana = ManzanaSerializer(many=True, source='manzana_set')

    class Meta:
        model = Proyecto
        fields = [
            'id_proyecto',
            'nombre_proyecto',
            'fecha_inicio',
            'fecha_fin',
            'id_manzana'
        ]


# Serializer del modelo PersonaProyecto
class PersonaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaProyecto
        fields = [
            'id_persona',
            'id_proyecto',
            'id_manzana',
            'id_lote',
            'id_cpagos'
        ]





# Serializer del modelo CronogramaPagos
class CronogramaPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronogramaPagos
        fields = [
            'id_cpagos',
            'descripcion_cpagos',
            'cuota_inicial',
            'cuota_mensual',
            'fecha_inicio_pago',
            'plazo_anios',
            'plazo_meses',
            'TEA', 
            'dias_pago',
            'descuento',
            'id_persona'
        ]


# Serializer del modelo Cuota
class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = [
            'id_cuota',
            'numero_cuotas',
            'fecha_vencimiento',
            'deuda_total',
            'amortizacion',
            'id_cpagos'
        ]


# Serializer del modelo Medio
class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = [
            'id_medio',
            'nombre_medio'
        ]


# Serializer del modelo Canal
class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = [
            'id_canal',
            'tipo_canal'
        ]


# Serializer del modelo Origen
class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = [
            'id_origen',
            'nombre_origen'
        ]


# Serializer del modelo Observaciones
class ObservacionesSerializer(serializers.ModelSerializer):
    id_persona = PersonaSerializer()

    class Meta:
        model = Observaciones
        fields = [
            'id_observaciones',
            'descripcion_observaciones',
            'adjuntar_informacion',
            'id_persona'
        ]
=======
from dataclasses import fields
from rest_framework import serializers
from .models import Area, Canal, ClienteCerrado, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Permiso, PermisoArea, Persona, PersonaProyecto, Programmer, Rol, Proyecto



class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'   
        
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'         
        
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__' 

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__' 

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__' 

class ManzanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzana
        fields = '__all__' 

class PersonaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaProyecto
        fields = '__all__' 

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__' 

class PermisoAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoArea
        fields = '__all__' 

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__' 

class ClienteCerradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteCerrado
        fields = '__all__' 
        
class CronogramaPagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronogramaPagos
        fields = '__all__' 

class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = '__all__' 

class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = '__all__' 

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = '__all__' 

class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__' 

class ObservacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observaciones
        fields = '__all__' 
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
