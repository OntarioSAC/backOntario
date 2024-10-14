from django.db import router
from django.urls import path, include
from rest_framework import routers
from api import views
from .views import PersonaAutocomplete, LoteAutocomplete, CpagosAutocomplete, VerificarYCriarCuotas



router=routers.DefaultRouter()
router.register(r'proyectos',views.ProyectoViewSet)                                 # Url del modelo Proyecto
router.register(r'personaclient',views.PersonaClientViewSet)                        # Url del modelo PersonaClient
router.register(r'lotes',views.LoteViewSet)                                         # Url del modelo Lote
router.register(r'fichadatosclientes',views.FichaDatosClienteViewSet)               # Url del modelo FichaDatosCliente
router.register(r'cronogramapagos',views.CronogramaPagosViewSet)                    # Url del modelo CronogramaPago
router.register(r'observaciones',views.ObservacionesViewSet)                        # Url del modelo Observaciones
router.register(r'cuotas',views.CuotaViewSet)                                       # Url del modelo Cuota
router.register(r'cuotainicialfraccionada',views.CuotaInicialFraccionadaViewSet)    # Url del modelo CuotaInicialFraccionada
router.register(r'detallepersona',views.DetallePersonaViewSet)                      # Url del modelo DetallePersona
router.register(r'empresa',views.EmpresaViewSet)                                    # Url del modelo Empresa
router.register(r'personastaff',views.PersonaStaffViewSet)                          # Url del modelo PersonaStaff
router.register(r'separacioncliente',views.SeparacionClienteViewSet)                # Url del modelo SeparacionCliente
router.register(r'observacionseparacion',views.ObservacionSeparacionViewSet)                # Url del modelo ObservacionSeparacion



urlpatterns=[
    path('', include(router.urls)),
    path('dataclient/',views.getData),
    path('get_cronograma_pagos/<int:id_fichadc>/', views.get_cronograma_pagos),
    path('dataproject/',views.get_proyectos),
    path('update_morosidad/<int:id_fichadc>/<int:id_cuota>/', views.putMorosidad),

    path('persona-autocomplete/', PersonaAutocomplete.as_view(), name='persona-autocomplete'),
    path('lote-autocomplete/', LoteAutocomplete.as_view(), name='lote-autocomplete'),
    path('cpagos-autocomplete/', CpagosAutocomplete.as_view(), name='cpagos-autocomplete'),
    path('verificar-y-crear-cuotas/', VerificarYCriarCuotas.as_view(), name='verificar_y_crear_cuotas'),
    path('login/', views.login, name='login'),  # Endpoint para el login

    # Endpoint para solicitar el restablecimiento de contraseña
    path('password-reset/request/', views.request_password_reset, name='password_reset_request'),

    # Endpoint para validar el token de restablecimiento de contraseña
    path('password-reset/validate/<str:token>/', views.validate_password_reset_token, name='password_reset_confirm'),

    # Endpoint para restablecer la contraseña
    path('password-reset/confirm/<str:token>/', views.reset_password, name='password_reset_complete'),

    path('get_lotes_libres/', views.get_lotes_libres, name='get_lotes_libres'),
    path('post_cliente_separacion/', views.post_cliente_separacion, name='post_cliente_separacion'),
    path('post_lote_conyuge/', views.post_lote_conyuge, name='post_lote_conyuge'),
    path('generate_boleta_code/', views.generate_boleta_code, name='post_lote_conyuge'),
    path('get_last_boleta_code/', views.get_last_boleta_code, name='get_last_boleta_code'),
    
]

