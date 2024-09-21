from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import CronogramaPagosSerializer, CuotaSerializer, LoteSerializer, ObservacionesSerializer, FichaDatosClienteSerializer, ProyectoSerializer, PersonaSerializer
from .models import CronogramaPagos, Cuota, Lote, Observaciones, Persona, FichaDatosCliente, Proyecto
from rest_framework.views import APIView
from django.db import connection
from datetime import date


from rest_framework.permissions import IsAuthenticated


# -----------------Pruebas
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import serializer


# -------------------------------

# View del modelo Proyecto
class ProyectoViewSet(viewsets.ModelViewSet):

    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    permission_classes = [IsAuthenticated]



# View del modelo Persona
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


@api_view(['GET'])
def getData(request):
    # Obtener todos los objetos de FichaDatosCliente
    fichas = FichaDatosCliente.objects.all()

    # Prepara la respuesta incluyendo los campos solicitados
    data = []
    for ficha in fichas:
        persona = ficha.id_persona  # Acceder al objeto Persona
        lote = ficha.id_lote        # Acceder al objeto Lote
        cpagos = ficha.id_cpagos    # Acceder al objeto CronogramaPagos
        proyecto = lote.id_proyecto # Acceder al proyecto asociado al lote

        # Inicializa morosidad y días de morosidad
        morosidad = False
        dias_morosidad = 0

        # Calcular la morosidad en base a los días de retraso
        cuotas = Cuota.objects.filter(id_cpagos=cpagos)

        if cuotas.exists():
            # Revisar cada cuota para determinar si alguna está en morosidad
            for cuota in cuotas:
                if cuota.fecha_pago_cuota and cuota.fecha_pago_cuota < date.today():
                    # Calcular los días de morosidad
                    dias_morosidad = (date.today() - cuota.fecha_pago_cuota).days

                    # Si los días de morosidad son mayores a 0, actualizar el estado si no está pagada
                    if dias_morosidad > 0:
                        cuota.dias_morosidad = dias_morosidad
                        if not cuota.estado:
                            cuota.estado = True  # Actualizar estado a True porque tiene morosidad
                        cuota.save()

            # Morosidad se determina en base a la última cuota en el ciclo
            morosidad = cuota.estado
        else:
            # Si no hay cuotas, morosidad y días de morosidad permanecen en False y 0 respectivamente
            morosidad = False
            dias_morosidad = 0

        # Prepara la estructura de la respuesta
        ficha_data = {
            'id_fichadc': ficha.id_fichadc,  # ID de la ficha
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'tipo_documento': persona.tipo_documento,
            'num_documento': persona.num_documento,
            'proyecto': proyecto.nombre_proyecto,  # Nombre del proyecto
            'lote': lote.manzana_lote,  # Lote asociado
            'morosidad': morosidad,  # Morosidad (True/False)
            'dias_morosidad': dias_morosidad  # Días de morosidad calculados
        }
        data.append(ficha_data)

    return Response(data)


@api_view(['GET'])
def get_cronograma_pagos(request, id_fichadc):
    try:
        # Obtener la ficha de datos del cliente por el ID
        ficha = FichaDatosCliente.objects.get(id_fichadc=id_fichadc)
        
        # Obtener el cronograma de pagos asociado a la ficha
        cronograma = ficha.id_cpagos
        
        # Obtener todas las cuotas relacionadas con el cronograma de pagos específico
        cuotas = Cuota.objects.filter(id_cpagos=cronograma)

        # Estructura de la respuesta con datos del cronograma y cuotas asociadas
        cronograma_data = {
            'id_cpagos': cronograma.id_cpagos,
            'cuota_inicial_dolares': cronograma.cuota_inicial_dolares,
            'cuota_inicial_soles': cronograma.cuota_inicial_soles,
            'fecha_pago_cuota': cronograma.fecha_pago_cuota,
            'fecha_inicio_pago': cronograma.fecha_inicio_pago,
            'descuento': cronograma.descuento,
            'precio_venta_soles': cronograma.precio_venta_soles,
            'precio_venta_dolares': cronograma.precio_venta_dolares,
            'deuda_total_soles': cronograma.deuda_total_soles,
            'deuda_total_dolares': cronograma.deuda_total_dolares,
            'TEA': cronograma.TEA,
            'observaciones': cronograma.observaciones,
            'tipo_cambio': cronograma.tipo_cambio,
            'numero_cuotas': cronograma.numero_cuotas,
            'numero_cuotas_pagadas': cronograma.numero_cuotas_pagadas,
            'cuotas': [
                {
                    'id_cuota': cuota.id_cuota,
                    'fecha_pago_cuota': cuota.fecha_pago_cuota,
                    'pago_adelantado': cuota.pago_adelantado,
                    'monto_pago_adelantado': cuota.monto_pago_adelantado,
                    'monto_cuota': cuota.monto_cuota,
                    'estado': cuota.estado,
                    'dias_morosidad': cuota.dias_morosidad,
                } for cuota in cuotas
            ]
        }

        # Retornar la respuesta con los datos del cronograma y las cuotas
        return Response(cronograma_data)

    except FichaDatosCliente.DoesNotExist:
        return Response({'error': 'Ficha de datos no encontrada.'}, status=404)


@api_view(['GET'])
def get_proyectos(request):
    # Obtener todos los proyectos
    proyectos = Proyecto.objects.all()

    # Prepara la respuesta incluyendo los campos solicitados
    data = []
    for proyecto in proyectos:
        # Obtener los lotes relacionados con cada proyecto
        lotes = Lote.objects.filter(id_proyecto=proyecto)

        # Prepara la estructura del proyecto con los lotes asociados
        proyecto_data = {
            'id_proyecto': proyecto.id_proyecto,
            'nombre_proyecto': proyecto.nombre_proyecto,
            'fecha_inicio': proyecto.fecha_inicio,
            'lotes': [
                {
                    'id_lote': lote.id_lote,
                    'manzana_lote': lote.manzana_lote,
                    'area': lote.area,
                    'perimetro': lote.perimetro,
                    'precio_lote_dolares': lote.precio_lote_dolares,
                    'precio_m2_dolares': lote.precio_m2_dolares,
                    'estado': lote.estado,
                } for lote in lotes
            ]
        }
        data.append(proyecto_data)

    # Retornar la respuesta con los datos de proyectos y lotes
    return Response(data)


# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
    # def get_queryset(self):
    #     # Filtro usando la relación de id_persona a través de FichaDatosCliente y la tabla Lote
    #     queryset = Lote.objects.filter(fichadatoscliente__id_persona__rol="Cliente Ontario")
    #     id_proyecto = self.request.query_params.get('id_proyecto', None)
    #     if id_proyecto is not None:
    #         queryset = queryset.filter(id_proyecto=id_proyecto)
    #     return queryset

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     id_lote = instance.id_lote
    #     self.perform_destroy(instance)
    #     if id_lote:
    #         id_lote.save()  # Re-enable the id_lote to be assignable again
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# View del modelo FichaDatosCliente
class FichaDatosClienteViewSet(viewsets.ModelViewSet):
    queryset = FichaDatosCliente.objects.all()
    serializer_class = FichaDatosClienteSerializer
    
    # def get_queryset(self):
    #     queryset = FichaDatosCliente.objects.filter(id_persona__id_rol__nombre_rol="Cliente Ontario")
    #     id_proyecto = self.request.query_params.get('id_proyecto', None)
    #     if id_proyecto is not None:
    #         queryset = queryset.filter(id_proyecto=id_proyecto)
    #     return queryset

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     id_cpagos = instance.id_cpagos
    #     self.perform_destroy(instance)
    #     if id_cpagos:
    #         id_cpagos.save()  # Re-enable the id_cpagos to be assignable again
    #     return Response(status=status.HTTP_204_NO_CONTENT)



# View del modelo CronogramaPagos
class CronogramaPagosViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPagos.objects.all()
    serializer_class = CronogramaPagosSerializer

    def get_queryset(self):
        # Aquí estás intentando filtrar por un proyecto o algún otro parámetro que esté relacionado con CronogramaPagos
        id_cpagos = self.request.query_params.get('id_cpagos', None)
        if id_cpagos is not None:
            queryset = CronogramaPagos.objects.filter(id_cpagos=id_cpagos)
        else:
            queryset = CronogramaPagos.objects.all()    
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        id_cpagos = instance.id_cpagos
        self.perform_destroy(instance)
        # No es necesario guardar el id_cpagos, pues no se reusa de esta manera en Django
        return Response(status=status.HTTP_204_NO_CONTENT)




# View del modelo Cuota
class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer


# View del modelo Observaciones
class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer



