from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import CronogramaPagosSerializer, CuotaSerializer, LoteSerializer, ObservacionesSerializer, FichaDatosClienteSerializer, ProyectoSerializer, PersonaSerializer
from .models import CronogramaPagos, Cuota, Lote, Observaciones, Persona, FichaDatosCliente, Proyecto
from rest_framework.views import APIView
from django.db import connection

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
        
        # Calcular morosidad: si hay deuda, es True
        morosidad = cpagos.deuda_total_soles > 0 or cpagos.deuda_total_dolares > 0
        
        # Prepara la estructura de la respuesta
        ficha_data = {
            'id_fichadc': ficha.id_fichadc,  # ID de la ficha
            'nombres': persona.nombres,
            'apellidos': persona.apellidos,
            'proyecto': proyecto.nombre_proyecto,  # Nombre del proyecto
            'lote': lote.manzana_lote,  # Lote asociado
            'morosidad': morosidad  # Morosidad (True/False)
        }
        data.append(ficha_data)

    return Response(data)




# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
    def get_queryset(self):
        # Filtro usando la relación de id_persona a través de FichaDatosCliente y la tabla Lote
        queryset = Lote.objects.filter(fichadatoscliente__id_persona__rol="Cliente Ontario")
        id_proyecto = self.request.query_params.get('id_proyecto', None)
        if id_proyecto is not None:
            queryset = queryset.filter(id_proyecto=id_proyecto)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        id_lote = instance.id_lote
        self.perform_destroy(instance)
        if id_lote:
            id_lote.save()  # Re-enable the id_lote to be assignable again
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
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



