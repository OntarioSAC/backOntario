from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import AreaSerializer, CanalSerializer, CronogramaPagosSerializer, CuotaSerializer, EstadoSerializer, LoteSerializer, ManzanaSerializer, MedioSerializer, ObservacionesSerializer, OrigenSerializer, PersonaProyectoSerializer, RolSerializer
from .serializer import ProyectoSerializer
from .serializer import PersonaSerializer
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Persona, PersonaProyecto, Rol
from .models import Proyecto
from rest_framework.views import APIView



    

# View del modelo Proyecto
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    

# View del modelo Persona
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


# View del modelo Rol
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


# View del modelo Estado
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
    
# View del modelo Manzana
class ManzanaViewSet(viewsets.ModelViewSet):
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer
    
    

class ProyectoManzanasView(APIView):
    def get(self, request, pk, format=None):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data)
    
    
# View del modelo PersonaProyecto
class PersonaProyectoViewSet(viewsets.ModelViewSet):
    queryset = PersonaProyecto.objects.all()
    serializer_class = PersonaProyectoSerializer
    
    def get_queryset(self):
        queryset = PersonaProyecto.objects.all()
        id_proyecto = self.request.query_params.get('id_proyecto', None)
        if id_proyecto is not None:
            queryset = queryset.filter(id_proyecto=id_proyecto)
        return queryset


# View del modelo Area
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


# View del modelo CronogramaPagos
class CronogramaPagosViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPagos.objects.all()
    serializer_class = CronogramaPagosSerializer


# View del modelo Cuota
class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer


# View del modelo Medio
class MedioViewSet(viewsets.ModelViewSet):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer


# View del modelo Canal
class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer


# View del modelo Origen
class OrigenViewSet(viewsets.ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer


# View del modelo Observaciones
class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer
