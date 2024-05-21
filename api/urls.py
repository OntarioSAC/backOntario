from django.db import router
from django.urls import URLPattern, path, include
from rest_framework import routers
from api import views


router=routers.DefaultRouter()
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
]
