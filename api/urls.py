from django.db import router
from django.urls import path, include
from rest_framework import routers
from api import views


router=routers.DefaultRouter()
router.register(r'proyectos',views.ProyectoViewSet)                     # Url del modelo Proyecto
router.register(r'personas',views.PersonaViewSet)                       # Url del modelo Persona
router.register(r'roles',views.RolViewSet)                              # Url del modelo Rol
router.register(r'lotes',views.LoteViewSet)                             # Url del modelo Lote
router.register(r'estados',views.EstadoViewSet)                         # Url del modelo Estado
router.register(r'manzanas',views.ManzanaViewSet)                       # Url del modelo Manzana
router.register(r'personaproyectos',views.PersonaProyectoViewSet)       # Url del modelo PersonaProyecto
router.register(r'areas',views.AreaViewSet)                             # Url del modelo Area
router.register(r'cronogramapagos',views.CronogramaPagosViewSet)        # Url del modelo CronogramaPago
router.register(r'cuotas',views.CuotaViewSet)                           # Url del modelo Cuota
router.register(r'medios',views.MedioViewSet)                           # Url del modelo Medio  
router.register(r'canales',views.CanalViewSet)                          # Url del modelo Canal
router.register(r'origenes',views.OrigenViewSet)                        # Url del modelo Origen
router.register(r'observaciones',views.ObservacionesViewSet)            # Url del modelo Observaciones


urlpatterns=[
    path('', include(router.urls)),
    path('proyecto/<int:pk>/manzanas/', views.ProyectoManzanasView.as_view(), name='proyecto-manzanas'),
    path('proyectos&manzanas/', views.ProyectoConManzanasView.as_view(), name='proyecto-con-manzanas'),
    path('manzanas&lotes/', views.ManzanaConLotesView.as_view(), name='manzanas-con-lotes'),
    path('lotes&estados/', views.LoteConEstadosView.as_view(), name='lotes-con-estados'),
    path('manzanas&lotes&estados/', views.ManzanaConLotesEstadosView.as_view(), name='manzanas-con-lotes-estados'),
    path('proyectos&manzanas&lotes&estados/', views.ProyectoConManzanasLotesEstadosView.as_view(), name='proyectos-con-manzanas-lotes-estados'),
]
