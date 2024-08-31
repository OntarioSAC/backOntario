from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import AreaSerializer, CanalSerializer, CronogramaPagosSerializer, CuotaSerializer, DocumentoSerializer, LoteSerializer, MedioSerializer, ObservacionesSerializer, OrigenSerializer, FichaDatosClienteSerializer, RolSerializer, UsuarioSerializer
from .serializer import ProyectoSerializer
from .serializer import PersonaSerializer
from .models import Area, Canal, CronogramaPagos, Cuota, Documento, Lote, Medio, Observaciones, Origen, Persona, FichaDatosCliente, Rol, Usuario
from .models import Proyecto
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


# -----------------Pruebas
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


# View del modelo Rol
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
    
# View del modelo FichaDatosCliente
class FichaDatosClienteViewSet(viewsets.ModelViewSet):
    queryset = FichaDatosCliente.objects.all()
    serializer_class = FichaDatosClienteSerializer
    
    def get_queryset(self):
        queryset = FichaDatosCliente.objects.filter(id_persona__id_rol__nombre_rol="Cliente Ontario")
        id_proyecto = self.request.query_params.get('id_proyecto', None)
        if id_proyecto is not None:
            queryset = queryset.filter(id_proyecto=id_proyecto)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        id_cpagos = instance.id_cpagos
        self.perform_destroy(instance)
        if id_cpagos:
            id_cpagos.save()  # Re-enable the id_cpagos to be assignable again
        return Response(status=status.HTTP_204_NO_CONTENT)


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


# View del modelo Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# View del modelo Documentos
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer