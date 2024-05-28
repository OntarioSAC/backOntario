<<<<<<< HEAD
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
=======
from rest_framework import viewsets
from .serializer import AreaSerializer, CanalSerializer, ClienteCerradoSerializer, CronogramaPagosSerializer, CuotaSerializer, EstadoSerializer, LoteSerializer, ManzanaSerializer, MedioSerializer, ObservacionesSerializer, OrigenSerializer, PermisoAreaSerializer, PermisoSerializer, PersonaProyectoSerializer, ProgrammerSerializer, RolSerializer
from .serializer import ProyectoSerializer
from .serializer import PersonaSerializer
from .models import Area, Canal, ClienteCerrado, CronogramaPagos, Cuota, Estado, Lote, Manzana, Medio, Observaciones, Origen, Permiso, PermisoArea, Persona, PersonaProyecto, Programmer, Rol
from .models import Proyecto

# Create your views here.


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

<<<<<<< HEAD

# View del modelo Rol
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

<<<<<<< HEAD

# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


# View del modelo Estado
=======
class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
<<<<<<< HEAD
    
# View del modelo Manzana
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class ManzanaViewSet(viewsets.ModelViewSet):
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer
    
<<<<<<< HEAD
    

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
=======
class PersonaProyectoViewSet(viewsets.ModelViewSet):
    queryset = PersonaProyecto.objects.all()
    serializer_class = PersonaProyectoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class PermisoAreaViewSet(viewsets.ModelViewSet):
    queryset = PermisoArea.objects.all()
    serializer_class = PermisoAreaSerializer
    
class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class ClienteCerradoViewSet(viewsets.ModelViewSet):
    queryset = ClienteCerrado.objects.all()
    serializer_class = ClienteCerradoSerializer

>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class CronogramaPagosViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPagos.objects.all()
    serializer_class = CronogramaPagosSerializer

<<<<<<< HEAD

# View del modelo Cuota
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer

<<<<<<< HEAD

# View del modelo Medio
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class MedioViewSet(viewsets.ModelViewSet):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer

<<<<<<< HEAD

# View del modelo Canal
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

<<<<<<< HEAD

# View del modelo Origen
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
class OrigenViewSet(viewsets.ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

<<<<<<< HEAD

# View del modelo Observaciones
class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer
=======
class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer

    
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
