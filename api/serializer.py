from rest_framework import serializers
from .models import CronogramaPagos, Cuota, FichaDatosCliente, Lote, Observaciones, Persona, Proyecto


class CustomModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {key: value for key, value in ret.items() if value}



# Serializer del modelo Persona
class PersonaSerializer(CustomModelSerializer):
    
    class Meta:
        model = Persona
        fields = [
            'id_persona',
            'nombres',
            'apellidos',
            'genero',
            'celular',
            'correo',
            'conyuge',
            'pais',
            'departamento',
            'provincia',
            'distrito',
            'fecha_creacion',
            'ocupacion',
            'centro_trabajo',
            'rol',
            'area',
            'origen',
            'canal',
            'medio',
            'usuario',
            'tipo_documento',
            'num_documento',
            'password',
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



# Serializer del modelo FichaDatosCliente
class FichaDatosClienteSerializer(CustomModelSerializer):
    persona = PersonaSerializer(source='id_persona')
    lote = LoteSerializer(source='id_lote')
    cpagos = CronogramaPagosSerializer(source='id_cpagos')
    
    class Meta:
        model = FichaDatosCliente
        fields = [
            'id_fichadc',
            'estado_legal',
            'persona',
            'lote',
            'cpagos'
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



# Serializer del modelo CuotaInicialFraccionada
class CuotaInicialFraccionadaSerializer(serializers.ModelSerializer):
    id_cpagos = CronogramaPagosSerializer()

    class Meta:
        model = Observaciones
        fields = [
            'id_cuota_inicial',
            'monto_inicial',
            'id_cpagos'
        ]