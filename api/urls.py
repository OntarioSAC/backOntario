from django.db import router
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import URLPattern, path, include
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
from rest_framework import routers
from api import views


router=routers.DefaultRouter()
<<<<<<< HEAD
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
=======
router.register(r'proyectos',views.ProyectoViewSet)
router.register(r'personas',views.PersonaViewSet)
router.register(r'roles',views.RolViewSet)
router.register(r'lotes',views.LoteViewSet)
router.register(r'estados',views.EstadoViewSet)
router.register(r'manzanas',views.ManzanaViewSet)
router.register(r'personaproyectos',views.PersonaProyectoViewSet)
router.register(r'areas',views.AreaViewSet)
router.register(r'permisoareas',views.PermisoAreaViewSet)
router.register(r'permiso',views.PermisoViewSet)
router.register(r'clientecerrados',views.ClienteCerradoViewSet)
router.register(r'cronogramapagos',views.CronogramaPagosViewSet)
router.register(r'cuotas',views.CuotaViewSet)
router.register(r'medios',views.MedioViewSet)
router.register(r'canales',views.CanalViewSet)
router.register(r'origenes',views.OrigenViewSet)
router.register(r'observaciones',views.ObservacionesViewSet)
# router.register(r'cronograma_pagos',views.CronogramaPagosSerializer)

urlpatterns=[
    path('', include(router.urls))
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
]
