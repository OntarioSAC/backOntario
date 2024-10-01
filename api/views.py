from dal import autocomplete
from datetime import datetime, date
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import CronogramaPagosSerializer, CuotaInicialFraccionadaSerializer, CuotaSerializer, LoteSerializer, ObservacionesSerializer, FichaDatosClienteSerializer, ProyectoSerializer, PersonaSerializer
from .models import CronogramaPagos, Cuota, CuotaInicialFraccionada, Lote, Observaciones, Persona, FichaDatosCliente, Proyecto
from rest_framework.views import APIView
from django.db import connection
from datetime import timedelta, date
from django.db.models import Q
import requests
from django.conf import settings



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


# View del modelo Persona
class CuotaInicialFraccionadaViewSet(viewsets.ModelViewSet):
    queryset = CuotaInicialFraccionada.objects.all()
    serializer_class = CuotaInicialFraccionadaSerializer



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

        # Inicializa morosidad general
        morosidad_general = False
        dias_morosidad_total = 0  # Inicializa los días de morosidad en 0

        # Obtener todas las cuotas del cronograma de pagos
        cuotas = Cuota.objects.filter(id_cpagos=cpagos).order_by('fecha_pago_cuota')

        # Revisamos todas las cuotas
        for cuota in cuotas:
            # Si la cuota no ha sido pagada (estado=True) y la fecha de pago ya ha pasado
            if cuota.estado:  # estado=True significa que no ha sido pagada
                # Calculamos los días de morosidad si la fecha de pago ya ha pasado
                dias_morosidad = (date.today() - cuota.fecha_pago_cuota).days

                # Solo consideramos morosidad si los días de morosidad son positivos
                if dias_morosidad > 0:
                    morosidad_general = True
                    dias_morosidad_total += dias_morosidad  # Sumamos los días de morosidad

                    # Actualiza la cuota con los días de morosidad y guarda
                    cuota.dias_morosidad = dias_morosidad
                    cuota.save()
                else:
                    # Si no hay morosidad (fecha futura), la dejamos en 0
                    cuota.dias_morosidad = 0
                    cuota.save()

        # Si no se encontraron cuotas morosas, los días de morosidad siguen siendo 0
        if not morosidad_general:
            dias_morosidad_total = 0

        # Prepara la estructura de la respuesta
        ficha_data = {
            'id_fichadc': ficha.id_fichadc,  # ID de la ficha
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'tipo_documento': persona.tipo_documento,
            'num_documento': persona.num_documento,
            'proyecto': proyecto.nombre_proyecto,  # Nombre del proyecto
            'lote': lote.manzana_lote,  # Lote asociado
            'morosidad': morosidad_general,  # Morosidad (True/False)
            'dias_morosidad': dias_morosidad_total  # Días de morosidad calculados en todas las cuotas morosas
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
            'tipo_cuota_inicial':cronograma.tipo_cuota_inicial,
            'tipo_moneda':cronograma.tipo_moneda,
            'cuotas': [
                {
                    'id_cuota': cuota.id_cuota,
                    'fecha_pago_cuota': cuota.fecha_pago_cuota,
                    'pago_adelantado': cuota.pago_adelantado,
                    'monto_pago_adelantado': cuota.monto_pago_adelantado,
                    'monto_cuota': cuota.monto_cuota,
                    'estado': cuota.estado,
                    'dias_morosidad': cuota.dias_morosidad,
                    'tipo_moneda': cuota.tipo_moneda
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


@api_view(['PUT'])
def putMorosidad(request, id_fichadc, id_cuota):
    try:
        # Buscar la ficha de datos cliente por ID
        ficha_cliente = FichaDatosCliente.objects.get(id_fichadc=id_fichadc)

        # Buscar la cuota específica asociada al cronograma de pagos de esta ficha
        cuota = Cuota.objects.get(id_cuota=id_cuota, id_cpagos=ficha_cliente.id_cpagos)

        # Obtener el cronograma de pagos asociado
        cronograma_pagos = ficha_cliente.id_cpagos

        # Obtener el nuevo estado del request
        nuevo_estado = request.data.get('estado', None)

        # Validar que el nuevo estado esté presente en la solicitud
        if nuevo_estado is None:
            return Response({"error": "El estado es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        # Actualizar el estado de la cuota
        cuota.estado = nuevo_estado

        # Si el estado es True (hay morosidad), recalcular los días de morosidad
        if cuota.estado:
            if cronograma_pagos.fecha_pago_cuota and cronograma_pagos.fecha_pago_cuota < date.today():
                dias_morosidad = (date.today() - cronograma_pagos.fecha_pago_cuota).days
                cuota.dias_morosidad = dias_morosidad
            else:
                cuota.dias_morosidad = 0  # Si la fecha es futura o hoy, no hay morosidad
        else:
            # Si no hay morosidad (estado False), poner días de morosidad en 0
            cuota.dias_morosidad = 0

        # Guardar los cambios en la cuota
        cuota.save()

        # Respuesta exitosa
        return Response({
            "message": f"Cuota {id_cuota} actualizada para la ficha {id_fichadc}",
            "estado": cuota.estado,
            "dias_morosidad": cuota.dias_morosidad
        }, status=status.HTTP_200_OK)

    except FichaDatosCliente.DoesNotExist:
        return Response({"error": "Ficha de datos cliente no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    except Cuota.DoesNotExist:
        return Response({"error": "Cuota no encontrada o no asociada a esta ficha"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Si el usuario no está autenticado, no devolver ningún resultado.
        if not self.request.user.is_authenticated:
            return Persona.objects.none()

        qs = Persona.objects.all()

        if self.q:
            # Buscar por nombres o num_documento
            qs = qs.filter(Q(nombres__icontains=self.q) | Q(num_documento__icontains=self.q))

        return qs

class LoteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Si el usuario no está autenticado, no devolver ningún resultado.
        if not self.request.user.is_authenticated:
            return Lote.objects.none()

        # Obtener todos los objetos de Lote
        qs = Lote.objects.all()

        if self.q:
            search_term = self.q.strip()

            # Usar un filtro de coincidencia exacta si se requiere precisión total
            qs = qs.filter(manzana_lote__iexact=search_term)

        return qs

class CpagosAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CronogramaPagos.objects.none()

        qs = CronogramaPagos.objects.all()

        if self.q:
            qs = qs.filter(id_cpagos__icontains=self.q)

        return qs
    

class VerificarYCriarCuotas(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener todos los cronogramas de pagos
        cronogramas = CronogramaPagos.objects.all()

        # Lista para almacenar resultados de los cronogramas procesados
        resultados = []

        for cronograma in cronogramas:
            # Obtener la última cuota del cronograma
            ultima_cuota = Cuota.objects.filter(id_cpagos=cronograma).order_by('-fecha_pago_cuota').first()

            if ultima_cuota:
                # Verificar si la fecha de la última cuota no es None y ya ha pasado
                if ultima_cuota.fecha_pago_cuota and ultima_cuota.fecha_pago_cuota < date.today():
                    # Si ha pasado, crear una nueva cuota 30 días después de la última
                    nueva_fecha_pago_cuota = ultima_cuota.fecha_pago_cuota + timedelta(days=30)

                    # Verificar si no excede el número de cuotas
                    cuotas_existentes = Cuota.objects.filter(id_cpagos=cronograma).count()
                    if cuotas_existentes < cronograma.numero_cuotas:
                        nueva_cuota = Cuota(
                            fecha_pago_cuota=nueva_fecha_pago_cuota,
                            id_cpagos=cronograma,
                            monto_cuota=ultima_cuota.monto_cuota,  # Ajusta esto si el monto varía
                            estado=True,  # Asumimos que está morosa inicialmente
                            tipo_moneda=ultima_cuota.tipo_moneda
                        )
                        nueva_cuota.save()
                        resultados.append(f"Nueva cuota creada para cronograma {cronograma.id_cpagos} con fecha {nueva_cuota.fecha_pago_cuota}")
                    else:
                        resultados.append(f"Ya se alcanzó el número máximo de cuotas para cronograma {cronograma.id_cpagos}")
                else:
                    if ultima_cuota.fecha_pago_cuota is None:
                        resultados.append(f"La última cuota del cronograma {cronograma.id_cpagos} no tiene fecha de pago")
                    else:
                        resultados.append(f"La última cuota del cronograma {cronograma.id_cpagos} aún no ha pasado")
            else:
                resultados.append(f"El cronograma {cronograma.id_cpagos} no tiene cuotas")

        return Response({"resultados": resultados})
