from rest_framework import serializers
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, FichaDatosCliente, Lote, Manzana, Medio, Observaciones, Origen, Persona, Rol, Proyecto, Usuario


class CustomModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {key: value for key, value in ret.items() if value is not None}

# Serializer del modelo Area
class AreaSerializer(CustomModelSerializer):
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
class PersonaSerializer(CustomModelSerializer):
    rol = RolSerializer(source='id_rol')
    area = AreaSerializer(source='id_area')
    
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
            'rol',
            'area',
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


class LoteSerializer(CustomModelSerializer):
    # id_estado = EstadoSerializer()

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
            # 'id_estado'
        ]


# Serializer del modelo Manzana
class ManzanaSerializer(CustomModelSerializer):
    # id_lote = LoteSerializer(many=True, source='lote_set')

    class Meta:
        model = Manzana
        fields = [
            'id_manzana',
            'nombre_manzana',
            # 'id_lote'
        ]


# Serializer del modelo Proyecto
class ProyectoSerializer(CustomModelSerializer):
    # id_manzana = ManzanaSerializer(many=True, source='manzana_set')

    class Meta:
        model = Proyecto
        fields = [
            'id_proyecto',
            'nombre_proyecto',
            'fecha_inicio',
            'fecha_fin',
            # 'id_manzana'
        ]



# Serializer del modelo CronogramaPagos
class CronogramaPagosSerializer(CustomModelSerializer):
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
            'descuento'
        ]

# Serializer del modelo FichaDatosCliente
class FichaDatosClienteSerializer(CustomModelSerializer):
    persona = PersonaSerializer(source='id_persona')
    proyecto = ProyectoSerializer(source='id_proyecto')
    manzana = ManzanaSerializer(source='id_manzana')
    lote = LoteSerializer(source='id_lote')
    cpagos = CronogramaPagosSerializer(source='id_cpagos')
    
    class Meta:
        model = FichaDatosCliente
        fields = [
            'persona',
            'proyecto',
            'manzana',
            'lote',
            'cpagos'
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

# Serializer del endpoint Proyectos&Manzanas
class ProyectoConManzanasSerializer(serializers.ModelSerializer):
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


class ManzanaConLotesSerializer(serializers.ModelSerializer):
    id_lote = LoteSerializer(many=True, source='lote_set')

    class Meta:
        model = Manzana
        fields = [
            'id_manzana', 
            'nombre_manzana', 
            'id_lote'
        ]

class LoteConEstadosSerializer(serializers.ModelSerializer):
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
        

class ManzanasConLotesEstadosSerializer(serializers.ModelSerializer):
    id_lote = LoteConEstadosSerializer(many=True, source='lote_set')

    class Meta:
        model = Manzana
        fields = [
            'id_manzana', 
            'nombre_manzana', 
            'id_lote'
        ]
        
class ProyectoConManzanasLotesEstadosSerializer(serializers.ModelSerializer):
    id_manzana = ManzanasConLotesEstadosSerializer(many=True, source='manzana_set')

    class Meta:
        model = Proyecto
        fields = [
            'id_proyecto',
            'nombre_proyecto',
            'fecha_inicio',
            'fecha_fin',
            'id_manzana'
        ]

# Serializer del modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'password'
        ]