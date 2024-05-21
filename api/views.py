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

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
class ManzanaViewSet(viewsets.ModelViewSet):
    queryset = Manzana.objects.all()
    serializer_class = ManzanaSerializer
    
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

class CronogramaPagosViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPagos.objects.all()
    serializer_class = CronogramaPagosSerializer

class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer

class MedioViewSet(viewsets.ModelViewSet):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer

class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class OrigenViewSet(viewsets.ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer

    
