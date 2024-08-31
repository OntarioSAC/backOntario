from django.db import router
from django.urls import path, include
from rest_framework import routers
from api import views


router=routers.DefaultRouter()
router.register(r'proyectos',views.ProyectoViewSet)                     # Url del modelo Proyecto
router.register(r'personas',views.PersonaViewSet)                       # Url del modelo Persona
router.register(r'roles',views.RolViewSet)                              # Url del modelo Rol
router.register(r'lotes',views.LoteViewSet)                             # Url del modelo Lote
router.register(r'fichadatosclientes',views.FichaDatosClienteViewSet)   # Url del modelo FichaDatosCliente
router.register(r'areas',views.AreaViewSet)                             # Url del modelo Area
router.register(r'cronogramapagos',views.CronogramaPagosViewSet)        # Url del modelo CronogramaPago
router.register(r'cuotas',views.CuotaViewSet)                           # Url del modelo Cuota
router.register(r'medios',views.MedioViewSet)                           # Url del modelo Medio  
router.register(r'canales',views.CanalViewSet)                          # Url del modelo Canal
router.register(r'origenes',views.OrigenViewSet)                        # Url del modelo Origen
router.register(r'observaciones',views.ObservacionesViewSet)            # Url del modelo Observaciones
router.register(r'usuarios',views.UsuarioViewSet)                       # Url del modelo Usuarios
router.register(r'documentos',views.DocumentoViewSet)                       # Url del modelo Usuarios


urlpatterns=[
    path('', include(router.urls)),
]
