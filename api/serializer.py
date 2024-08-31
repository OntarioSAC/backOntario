from rest_framework import serializers
from .models import Area, Canal, CronogramaPagos, Cuota, Documento, FichaDatosCliente, Lote, Medio, Observaciones, Origen, Persona, Rol, Proyecto, Usuario


class CustomModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {key: value for key, value in ret.items() if value}

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
class RolSerializer(CustomModelSerializer):
    class Meta:
        model = Rol
        fields = [
            'id_rol',
            'nombre_rol'
        ]

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

# Serializer del modelo Documento
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = [
            'id_documento',
            'nombre_documento'
        ]

# Serializer del modelo Persona
class PersonaSerializer(CustomModelSerializer):
    # rol = RolSerializer(source='id_rol', required=False, allow_null=True)
    # area = AreaSerializer(source='id_area', required=False, allow_null=True)
    # origen = OrigenSerializer(source='id_origen', required=False, allow_null=True)
    # canal = CanalSerializer(source='id_canal', required=False, allow_null=True)
    # medio = MedioSerializer(source='id_medio', required=False, allow_null=True)
    # documento = DocumentoSerializer(source='id_documento', required=False, allow_null=True)
    
    class Meta:
        model = Persona
        fields = [
            'id_persona',
            'nombres',
            'apellidos',
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
            'id_medio',
            'id_documento',
        ]

    def validate(self, data):
        # Obtener el valor del documento y dni
        documento = data.get('id_documento')
        dni = data.get('DNI')

        # Verificar si el documento es DNI
        if documento and documento.nombre_documento == 'DNI':
            if dni and len(dni) != 8:
                raise serializers.ValidationError("El campo DNI debe tener exactamente 8 caracteres.")
        
        return data






# Serializer del modelo Proyecto
class ProyectoSerializer(CustomModelSerializer):

    class Meta:
        model = Proyecto
        fields = [
            'id_proyecto',
            'nombre_proyecto',
            'fecha_inicio',
        ]


# Serializer del modelo Lote

class LoteSerializer(CustomModelSerializer):
    # proyecto = ProyectoSerializer(source='id_proyecto')

    class Meta:
        model = Lote
        fields = [
            'id_lote',
            'manzana_lote',
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
            'estado',
            'id_proyecto'
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
    lote = LoteSerializer(source='id_lote')
    cuota = CronogramaPagosSerializer(source='id_cuota')
    
    class Meta:
        model = FichaDatosCliente
        fields = [
            'persona',
            'lote',
            'cuota'
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



# Serializer del modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'password'
        ]