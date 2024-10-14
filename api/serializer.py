from rest_framework import serializers
from .models import CronogramaPagos, Cuota, CuotaInicialFraccionada, DetallePersona, Empresa, FichaDatosCliente, Lote, Observaciones, PersonaClient, PersonaStaff, Proyecto, SeparacionCliente
from django.contrib.auth.hashers import check_password




class CustomModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {key: value for key, value in ret.items() if value}



# Serializer del modelo PersonaClient
class PersonaClientSerializer(CustomModelSerializer):
    
    class Meta:
        model = PersonaClient
        fields = [
            'id_persona_client',
            'nombres',
            'apellidos',
            'genero',
            'celular',
            'correo',
            'pais',
            'departamento',
            'provincia',
            'distrito',
            'fecha_creacion',
            'ocupacion',
            'centro_trabajo',
            'tipo_documento',
            'num_documento',
            'conyuge',
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
            'imagen',
        ]


# Serializer del modelo Lote

class LoteSerializer(CustomModelSerializer):
    proyecto = ProyectoSerializer(source='id_proyecto')

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
            'precio_lote_dolares',
            'precio_m2_dolares',
            'estado',
            'proyecto'
        ]



# Serializer del modelo CronogramaPagos
class CronogramaPagosSerializer(CustomModelSerializer):
    class Meta:
        model = CronogramaPagos
        fields = [
            'id_cpagos',
            'cuota_inicial_dolares',
            'cuota_inicial_soles',
            'fecha_pago_cuota',
            'fecha_inicio_pago',
            'descuento',
            'precio_venta_soles',
            'precio_venta_dolares',
            'precio_m2_soles',
            'precio_m2_dolares',
            'deuda_total_soles', 
            'deuda_total_dolares', 
            'TEA',
            'observaciones',
            'tipo_cambio',
            'numero_cuotas',
            'numero_cuotas_pagadas',
            'tipo_cuota_inicial',
        ]



# Serializer del modelo Cuota
class CuotaSerializer(CustomModelSerializer):
    cpagos = CronogramaPagosSerializer(source='id_cpagos')

    class Meta:
        model = Cuota
        fields = [
            'id_cuota',
            'fecha_pago_cuota',
            'pago_adelantado',
            'monto_pago_adelantado',
            'monto_cuota',
            'cpagos',
        ]



# Serializer del modelo DatosPersona
class FichaDatosClienteSerializer(CustomModelSerializer):
    # persona = PersonaSerializer(source='id_persona')
    lote = LoteSerializer(source='id_lote')
    cpagos = CronogramaPagosSerializer(source='id_cpagos')
    
    class Meta:
        model = FichaDatosCliente
        fields = [
            'id_fichadc',
            'estado_legal',
            'fecha_cierre',
            'fecha_separacion',
            'fecha_limite_separacion',
            'cod_boleta',
            'asesor',
            'lote',
            'cpagos'
        ]



# Serializer del modelo Observaciones
class ObservacionesSerializer(serializers.ModelSerializer):
    persona = PersonaClientSerializer(source='id_persona_client')

    class Meta:
        model = Observaciones
        fields = [
            'id_observaciones',
            'descripcion_observaciones',
            'adjuntar_informacion',
            'persona'
        ]



# Serializer del modelo CuotaInicialFraccionada
class CuotaInicialFraccionadaSerializer(serializers.ModelSerializer):
    cpagos = CronogramaPagosSerializer(source='id_cpagos')

    class Meta:
        model = CuotaInicialFraccionada
        fields = [
            'id_cuota_inicial',
            'monto_inicial',
            'cpagos'
        ]


# Serializer del modelo DetallePersona
class DetallePersonaSerializer(serializers.ModelSerializer):
    persona_client = PersonaClientSerializer(source='id_persona_client')
    fichadc = FichaDatosClienteSerializer(source='id_fichadc')

    class Meta:
        model = DetallePersona
        fields = [
            'id_detalle_persona',
            'tipo_cliente',
            'usuario',
            'canal',
            'medio',
            'area',
            'origen',
            'persona_client',
            'fichadc'
        ]


# Serializer del modelo Empresa
class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = [
            'id_empresa',
            'nombre_empresa',
            'ruc'
        ]


# Serializer del modelo PersonaStaff
class PersonaStaffSerializer(CustomModelSerializer):
    empresa = EmpresaSerializer(source='id_empresa')


    class Meta:
        model = PersonaStaff
        fields = [
            'id_persona_staff',
            'nombres',
            'apellidos',
            'area',
            'dni',
            'conyuge',
            'correo',
            'celular',
            'fecha_inicio',
            'fecha_fin',
            'foto',
            'centro_costos',
            'empresa'
        ]


# Serializer del modelo SeparacionCliente
class SeparacionClienteSerializer(CustomModelSerializer):
    fichadc = FichaDatosClienteSerializer(source='id_fichadc')

    class Meta:
        model = SeparacionCliente
        fields = [
            'id_separacion',
            'fecha_separacion',
            'fecha_limite_separacion',
            'monto_separacion',
            'estado_separacion',
            'fichadc'
        ]


# Serializer del modelo SeparacionCliente
class ObservacionSeparacionSerializer(CustomModelSerializer):
    separacion = SeparacionClienteSerializer(source='id_separacion')

    class Meta:
        model = SeparacionCliente
        fields = [
            'id_observacion',
            'descripcion',
            'fecha_creacion',
            'separacion',
          ]