from django.db import router
from django.urls import path, include
from rest_framework import routers
from api import views
from .views import PersonaAutocomplete, LoteAutocomplete, CpagosAutocomplete

router=routers.DefaultRouter()
router.register(r'proyectos',views.ProyectoViewSet)                     # Url del modelo Proyecto
router.register(r'personas',views.PersonaViewSet)                       # Url del modelo Persona
router.register(r'lotes',views.LoteViewSet)                             # Url del modelo Lote
router.register(r'fichadatosclientes',views.FichaDatosClienteViewSet)   # Url del modelo FichaDatosCliente
router.register(r'cronogramapagos',views.CronogramaPagosViewSet)        # Url del modelo CronogramaPago
router.register(r'observaciones',views.ObservacionesViewSet)            # Url del modelo Observaciones
router.register(r'cuotas',views.CuotaViewSet)                           # Url del modelo Cuota



urlpatterns=[
    path('', include(router.urls)),
    path('dataclient/',views.getData),
    path('get_cronograma_pagos/<int:id_fichadc>/', views.get_cronograma_pagos),
    path('dataproject/',views.get_proyectos),
    path('update_morosidad/<int:id_fichadc>/<int:id_cuota>/', views.putMorosidad),
    
    path('persona-autocomplete/', PersonaAutocomplete.as_view(), name='persona-autocomplete'),
    path('lote-autocomplete/', LoteAutocomplete.as_view(), name='lote-autocomplete'),
    path('cpagos-autocomplete/', CpagosAutocomplete.as_view(), name='cpagos-autocomplete'),
]

