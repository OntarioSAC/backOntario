from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import AreaSerializer, CanalSerializer, CronogramaPagosSerializer, CuotaSerializer, EstadoSerializer, LoteConEstadosSerializer, LoteSerializer, ManzanaConLotesSerializer, ManzanaSerializer, ManzanasConLotesEstadosSerializer, MedioSerializer, ObservacionesSerializer, OrigenSerializer, FichaDatosClienteSerializer, ProyectoConManzanasLotesEstadosSerializer, ProyectoConManzanasSerializer, RolSerializer
from .serializer import ProyectoSerializer
from .serializer import PersonaSerializer
from .models import Area, Canal, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Persona, FichaDatosCliente, Rol
from .models import Proyecto
from rest_framework.views import APIView

# -----------------Pruebas
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def manzanas_por_proyecto(request, proyecto_id):
    manzanas = Manzana.objects.filter(id_proyecto=proyecto_id)
    serializer = ManzanaSerializer(manzanas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lotes_por_manzana(request, manzana_id):
    lotes = Lote.objects.filter(id_manzana=manzana_id, id_estado_id=1)
    serializer = LoteSerializer(lotes, many=True)
    return Response(serializer.data)

# -------------------------------

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
    
    
# View del modelo FichaDatosCliente
class FichaDatosClienteViewSet(viewsets.ModelViewSet):
    queryset = FichaDatosCliente.objects.all()
    serializer_class = FichaDatosClienteSerializer
    
    def get_queryset(self):
        queryset = FichaDatosCliente.objects.all()
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


# View del endpoint Proyectos&Manzanas
class ProyectoConManzanasView(APIView):
    def get(self, request, format=None):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoConManzanasSerializer(proyectos, many=True)
        return Response(serializer.data)
    

# View del endpoint Manzanas&Lotes
class ManzanaConLotesView(APIView):
    def get(self, request, format=None):
        manzanas = Manzana.objects.all()
        serializer = ManzanaConLotesSerializer(manzanas, many=True)
        return Response(serializer.data)    
    
# View del endpoint Manzanas&Lotes
class LoteConEstadosView(APIView):
    def get(self, request, format=None):
        lotes = Lote.objects.all()
        serializer = LoteConEstadosSerializer(lotes, many=True)
        return Response(serializer.data) 
    
    
class ManzanaConLotesEstadosView(APIView):
    def get(self, request, format=None):
        manzanas = Manzana.objects.all()
        serializer = ManzanasConLotesEstadosSerializer(manzanas, many=True)
        return Response(serializer.data)
    
class ProyectoConManzanasLotesEstadosView(APIView):
    def get(self, request, format=None):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoConManzanasLotesEstadosSerializer(proyectos, many=True)
        return Response(serializer.data)