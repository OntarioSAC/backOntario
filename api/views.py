from dal import autocomplete
from datetime import datetime, date
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializer import CronogramaPagosSerializer, CuotaInicialFraccionadaSerializer, CuotaSerializer, DetallePersonaSerializer, EmpresaSerializer, LoteSerializer, ObservacionSeparacionSerializer, ObservacionesSerializer, FichaDatosClienteSerializer, PersonaClientSerializer, PersonaStaffSerializer, ProyectoSerializer
from .models import CronogramaPagos, Cuota, CuotaInicialFraccionada, DetallePersona, Empresa, Lote, ObservacionSeparacion, Observaciones, FichaDatosCliente, PersonaClient, PersonaStaff, Proyecto, SeparacionCliente
from rest_framework.views import APIView
from django.db import connection
from datetime import timedelta, date
from django.db.models import Q
from django.conf import settings

from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
from .models import PasswordResetToken

from django.db import transaction
from django.utils import timezone

from dateutil.relativedelta import relativedelta  # Manejo de meses precisos
from rest_framework.pagination import PageNumberPagination


import jwt


# -----------------Pruebas
from rest_framework.decorators import api_view
from rest_framework.response import Response
# -------------------------------


# View del modelo Proyecto
class ProyectoViewSet(viewsets.ModelViewSet):

    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    # permission_classes = [IsAuthenticated]



# View del modelo PersonaClient
class PersonaClientViewSet(viewsets.ModelViewSet):
    queryset = PersonaClient.objects.all()
    serializer_class = PersonaClientSerializer


# View del modelo CuotaInicialFraccionada
class CuotaInicialFraccionadaViewSet(viewsets.ModelViewSet):
    queryset = CuotaInicialFraccionada.objects.all()
    serializer_class = CuotaInicialFraccionadaSerializer



# @api_view(['GET'])
# def getData(request):
#     # Obtener todos los objetos de FichaDatosCliente
#     fichas = FichaDatosCliente.objects.all()

#     # Prepara la respuesta incluyendo los campos solicitados
#     data = []
#     for ficha in fichas:
#         lote = ficha.id_lote        # Acceder al objeto Lote
#         cpagos = ficha.id_cpagos    # Acceder al objeto CronogramaPagos
#         proyecto = lote.id_proyecto # Acceder al proyecto asociado al lote

#         # Obtener todas las personas relacionadas a través de DetallePersona
#         detalles_persona = DetallePersona.objects.filter(id_fichadc=ficha.id_fichadc)

#         personas_data = []
#         for detalle in detalles_persona:
#             persona = detalle.id_persona_client  # Acceder al objeto PersonaClient
#             # Prepara los datos de cada persona relacionada
#             personas_data.append({
#                 'nombres': persona.nombres,
#                 'apellidos': persona.apellidos,
#                 'tipo_documento': persona.tipo_documento,
#                 'num_documento': persona.num_documento,
#                 'tipo_cliente': detalle.tipo_cliente,
#                 'canal': detalle.canal,
#                 'medio': detalle.medio,
#             })

#         # Inicializa morosidad general
#         morosidad_general = False
#         dias_morosidad_total = 0  # Inicializa los días de morosidad en 0

#         # Obtener todas las cuotas del cronograma de pagos
#         cuotas = Cuota.objects.filter(id_cpagos=cpagos).order_by('fecha_pago_cuota')

#         # Revisamos todas las cuotas
#         for cuota in cuotas:
#             # Si la cuota no ha sido pagada (estado=True) y la fecha de pago ya ha pasado
#             if cuota.estado:  # estado=True significa que no ha sido pagada
#                 # Calculamos los días de morosidad si la fecha de pago ya ha pasado
#                 dias_morosidad = (date.today() - cuota.fecha_pago_cuota).days

#                 # Solo consideramos morosidad si los días de morosidad son positivos
#                 if dias_morosidad > 0:
#                     morosidad_general = True
#                     dias_morosidad_total += dias_morosidad  # Sumamos los días de morosidad

#                     # Actualiza la cuota con los días de morosidad y guarda
#                     cuota.dias_morosidad = dias_morosidad
#                     cuota.save()
#                 else:
#                     # Si no hay morosidad (fecha futura), la dejamos en 0
#                     cuota.dias_morosidad = 0
#                     cuota.save()

#         # Si no se encontraron cuotas morosas, los días de morosidad siguen siendo 0
#         if not morosidad_general:
#             dias_morosidad_total = 0

#         # Prepara la estructura de la respuesta
#         ficha_data = {
#             'id_fichadc': ficha.id_fichadc,  # ID de la ficha
#             'proyecto': proyecto.nombre_proyecto,  # Nombre del proyecto
#             'lote': lote.manzana_lote,  # Lote asociado
#             'morosidad': cuota.estado,  # Morosidad (True/False)
#             'dias_morosidad': dias_morosidad_total,  # Días de morosidad calculados en todas las cuotas morosas
#             'personas': personas_data  # Lista de personas relacionadas con el lote
#         }
#         data.append(ficha_data)

#     return Response(data)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30  # Establece el tamaño de página por defecto a 30
    # Si no deseas permitir que el cliente cambie el tamaño de página, comenta o elimina la siguiente línea:
    # page_size_query_param = 'page_size'
    # Establece el tamaño máximo de página permitido:
    max_page_size = 30

@api_view(['GET'])
def getData(request):
    paginator = StandardResultsSetPagination()
    fichas = FichaDatosCliente.objects.select_related('id_lote', 'id_cpagos', 'id_lote__id_proyecto').prefetch_related('detallepersona_set')
    
    result_page = paginator.paginate_queryset(fichas, request)
    
    data = []
    for ficha in result_page:
        lote = ficha.id_lote
        cpagos = ficha.id_cpagos
        proyecto = lote.id_proyecto

        personas_data = [
            {
                'nombres': detalle.id_persona_client.nombres,
                'apellidos': detalle.id_persona_client.apellidos,
                'tipo_documento': detalle.id_persona_client.tipo_documento,
                'num_documento': detalle.id_persona_client.num_documento,
                'tipo_cliente': detalle.tipo_cliente,
                'canal': detalle.canal,
                'medio': detalle.medio,
            }
            for detalle in ficha.detallepersona_set.all()
        ]

        cuotas = Cuota.objects.filter(id_cpagos=cpagos).order_by('fecha_pago_cuota')
        morosidad_general = False
        dias_morosidad_total = 0

        for cuota in cuotas:
            if cuota.estado and (date.today() > cuota.fecha_pago_cuota):
                dias_morosidad = (date.today() - cuota.fecha_pago_cuota).days
                if dias_morosidad > 0:
                    morosidad_general = True
                    dias_morosidad_total += dias_morosidad

        ficha_data = {
            'id_fichadc': ficha.id_fichadc,
            'proyecto': proyecto.nombre_proyecto,
            'lote': lote.manzana_lote,
            'morosidad': morosidad_general,
            'dias_morosidad': dias_morosidad_total,
            'personas': personas_data
        }
        data.append(ficha_data)

    # Agrega la información del total de páginas y del total de elementos
    response = paginator.get_paginated_response(data)
    response.data['total_pages'] = paginator.page.paginator.num_pages  # Total de páginas
    response.data['total_items'] = paginator.page.paginator.count  # Total de elementos

    return response


@api_view(['GET'])
def get_cronograma_pagos(request, id_fichadc):
    try:
        # Obtener la ficha de datos del cliente por el ID
        ficha = FichaDatosCliente.objects.get(id_fichadc=id_fichadc)
        
        # Obtener el cronograma de pagos asociado a la ficha
        cronograma = ficha.id_cpagos
        
        # Obtener todas las cuotas relacionadas con el cronograma de pagos específico
        cuotas = Cuota.objects.filter(id_cpagos=cronograma)

        # Estructura de la respuesta con datos del cronograma y cuotas asociadas
        cronograma_data = {
            'id_cpagos': cronograma.id_cpagos,
            'cuota_inicial_dolares': cronograma.cuota_inicial_dolares,
            'cuota_inicial_soles': cronograma.cuota_inicial_soles,
            'fecha_pago_cuota': cronograma.fecha_pago_cuota,
            'fecha_inicio_pago': cronograma.fecha_inicio_pago,
            'descuento': cronograma.descuento,
            'precio_venta_soles': cronograma.precio_venta_soles,
            'precio_venta_dolares': cronograma.precio_venta_dolares,
            'deuda_total_soles': cronograma.deuda_total_soles,
            'deuda_total_dolares': cronograma.deuda_total_dolares,
            'TEA': cronograma.TEA,
            'observaciones': cronograma.observaciones,
            'tipo_cambio': cronograma.tipo_cambio,
            'numero_cuotas': cronograma.numero_cuotas,
            'numero_cuotas_pagadas': cronograma.numero_cuotas_pagadas,
            'tipo_cuota_inicial':cronograma.tipo_cuota_inicial,
            'tipo_moneda':cronograma.tipo_moneda,
            'cuotas': [
                {
                    'id_cuota': cuota.id_cuota,
                    'fecha_pago_cuota': cuota.fecha_pago_cuota,
                    'pago_adelantado': cuota.pago_adelantado,
                    'monto_pago_adelantado': cuota.monto_pago_adelantado,
                    'monto_cuota': cuota.monto_cuota,
                    'estado': cuota.estado,
                    'dias_morosidad': cuota.dias_morosidad,
                    'tipo_moneda': cuota.tipo_moneda
                } for cuota in cuotas
            ]
        }

        # Retornar la respuesta con los datos del cronograma y las cuotas
        return Response(cronograma_data)

    except FichaDatosCliente.DoesNotExist:
        return Response({'error': 'Ficha de datos no encontrada.'}, status=404)


@api_view(['GET'])
def get_proyectos(request):
    # Obtener todos los proyectos
    proyectos = Proyecto.objects.all()

    # Prepara la respuesta incluyendo los campos solicitados
    data = []
    for proyecto in proyectos:
        # Obtener los lotes relacionados con cada proyecto
        lotes = Lote.objects.filter(id_proyecto=proyecto)

        # Obtener la URL completa de la imagen si existe
        imagen_url = (
            request.build_absolute_uri(proyecto.imagen.url)
            if proyecto.imagen else None
        )

        # Prepara la estructura del proyecto con los lotes asociados
        proyecto_data = {
            'id_proyecto': proyecto.id_proyecto,
            'nombre_proyecto': proyecto.nombre_proyecto,
            'fecha_inicio': proyecto.fecha_inicio,
            'imagen': imagen_url,
            'lotes': [
                {
                    'id_lote': lote.id_lote,
                    'manzana_lote': lote.manzana_lote,
                    'area': lote.area,
                    'perimetro': lote.perimetro,
                    'precio_lote_dolares': lote.precio_lote_dolares,
                    'precio_m2_dolares': lote.precio_m2_dolares,
                    'estado': lote.estado,
                } for lote in lotes
            ]
        }
        data.append(proyecto_data)

    # Retornar la respuesta con los datos de proyectos y lotes
    return Response(data)


# View del modelo Lote
class LoteViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    
    # def get_queryset(self):
    #     # Filtro usando la relación de id_persona a través de FichaDatosCliente y la tabla Lote
    #     queryset = Lote.objects.filter(fichadatoscliente__id_persona__rol="Cliente Ontario")
    #     id_proyecto = self.request.query_params.get('id_proyecto', None)
    #     if id_proyecto is not None:
    #         queryset = queryset.filter(id_proyecto=id_proyecto)
    #     return queryset

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     id_lote = instance.id_lote
    #     self.perform_destroy(instance)
    #     if id_lote:
    #         id_lote.save()  # Re-enable the id_lote to be assignable again
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# View del modelo FichaDatosCliente
class FichaDatosClienteViewSet(viewsets.ModelViewSet):
    queryset = FichaDatosCliente.objects.all()
    serializer_class = FichaDatosClienteSerializer
    
    # def get_queryset(self):
    #     queryset = FichaDatosCliente.objects.filter(id_persona__id_rol__nombre_rol="Cliente Ontario")
    #     id_proyecto = self.request.query_params.get('id_proyecto', None)
    #     if id_proyecto is not None:
    #         queryset = queryset.filter(id_proyecto=id_proyecto)
    #     return queryset

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     id_cpagos = instance.id_cpagos
    #     self.perform_destroy(instance)
    #     if id_cpagos:
    #         id_cpagos.save()  # Re-enable the id_cpagos to be assignable again
    #     return Response(status=status.HTTP_204_NO_CONTENT)



# View del modelo CronogramaPagos
class CronogramaPagosViewSet(viewsets.ModelViewSet):
    queryset = CronogramaPagos.objects.all()
    serializer_class = CronogramaPagosSerializer

    def get_queryset(self):
        # Aquí estás intentando filtrar por un proyecto o algún otro parámetro que esté relacionado con CronogramaPagos
        id_cpagos = self.request.query_params.get('id_cpagos', None)
        if id_cpagos is not None:
            queryset = CronogramaPagos.objects.filter(id_cpagos=id_cpagos)
        else:
            queryset = CronogramaPagos.objects.all()    
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        id_cpagos = instance.id_cpagos
        self.perform_destroy(instance)
        # No es necesario guardar el id_cpagos, pues no se reusa de esta manera en Django
        return Response(status=status.HTTP_204_NO_CONTENT)




# View del modelo Cuota
class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer


# View del modelo Observaciones
class ObservacionesViewSet(viewsets.ModelViewSet):
    queryset = Observaciones.objects.all()
    serializer_class = ObservacionesSerializer


@api_view(['PUT'])
def putMorosidad(request, id_fichadc, id_cuota):
    try:
        # Buscar la ficha de datos cliente por ID
        ficha_cliente = FichaDatosCliente.objects.get(id_fichadc=id_fichadc)

        # Buscar la cuota específica asociada al cronograma de pagos de esta ficha
        cuota = Cuota.objects.get(id_cuota=id_cuota, id_cpagos=ficha_cliente.id_cpagos)

        # Obtener el cronograma de pagos asociado
        cronograma_pagos = ficha_cliente.id_cpagos

        # Obtener el nuevo estado del request
        nuevo_estado = request.data.get('estado', None)

        # Validar que el nuevo estado esté presente en la solicitud
        if nuevo_estado is None:
            return Response({"error": "El estado es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        # Actualizar el estado de la cuota
        cuota.estado = nuevo_estado

        # Si el estado es True (hay morosidad), recalcular los días de morosidad
        if cuota.estado:
            if cronograma_pagos.fecha_pago_cuota and cronograma_pagos.fecha_pago_cuota < date.today():
                dias_morosidad = (date.today() - cronograma_pagos.fecha_pago_cuota).days
                cuota.dias_morosidad = dias_morosidad
            else:
                cuota.dias_morosidad = 0  # Si la fecha es futura o hoy, no hay morosidad
        else:
            # Si no hay morosidad (estado False), poner días de morosidad en 0
            cuota.dias_morosidad = 0

        # Guardar los cambios en la cuota
        cuota.save()

        # Respuesta exitosa
        return Response({
            "message": f"Cuota {id_cuota} actualizada para la ficha {id_fichadc}",
            "estado": cuota.estado,
            "dias_morosidad": cuota.dias_morosidad
        }, status=status.HTTP_200_OK)

    except FichaDatosCliente.DoesNotExist:
        return Response({"error": "Ficha de datos cliente no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    except Cuota.DoesNotExist:
        return Response({"error": "Cuota no encontrada o no asociada a esta ficha"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Si el usuario no está autenticado, no devolver ningún resultado.
        if not self.request.user.is_authenticated:
            return PersonaClient.objects.none()

        qs = PersonaClient.objects.all()

        if self.q:
            # Buscar por nombres o num_documento
            qs = qs.filter(Q(nombres__icontains=self.q) | Q(num_documento__icontains=self.q))

        return qs

class LoteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Si el usuario no está autenticado, no devolver ningún resultado.
        if not self.request.user.is_authenticated:
            return Lote.objects.none()

        # Obtener todos los objetos de Lote
        qs = Lote.objects.all()

        if self.q:
            search_term = self.q.strip()

            # Usar un filtro de coincidencia exacta si se requiere precisión total
            qs = qs.filter(manzana_lote__iexact=search_term)

        return qs

class CpagosAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CronogramaPagos.objects.none()

        qs = CronogramaPagos.objects.all()

        if self.q:
            qs = qs.filter(id_cpagos__icontains=self.q)

        return qs
    

class VerificarYCriarCuotas(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener todos los cronogramas de pagos
        cronogramas = CronogramaPagos.objects.all()

        # Lista para almacenar resultados de los cronogramas procesados
        resultados = []

        for cronograma in cronogramas:
            # Obtener la última cuota del cronograma
            ultima_cuota = Cuota.objects.filter(id_cpagos=cronograma).order_by('-fecha_pago_cuota').first()

            if ultima_cuota:
                # Verificar si la fecha de la última cuota no es None y ya ha pasado
                if ultima_cuota.fecha_pago_cuota and ultima_cuota.fecha_pago_cuota < date.today():
                    # Si ha pasado, crear una nueva cuota 30 días después de la última
                    nueva_fecha_pago_cuota = ultima_cuota.fecha_pago_cuota + timedelta(days=30)

                    # Verificar si no excede el número de cuotas
                    cuotas_existentes = Cuota.objects.filter(id_cpagos=cronograma).count()
                    if cuotas_existentes < cronograma.numero_cuotas:
                        nueva_cuota = Cuota(
                            fecha_pago_cuota=nueva_fecha_pago_cuota,
                            id_cpagos=cronograma,
                            monto_cuota=ultima_cuota.monto_cuota,  # Ajusta esto si el monto varía
                            estado=True,  # Asumimos que está morosa inicialmente
                            tipo_moneda=ultima_cuota.tipo_moneda
                        )
                        nueva_cuota.save()
                        resultados.append(f"Nueva cuota creada para cronograma {cronograma.id_cpagos} con fecha {nueva_cuota.fecha_pago_cuota}")
                    else:
                        resultados.append(f"Ya se alcanzó el número máximo de cuotas para cronograma {cronograma.id_cpagos}")
                else:
                    if ultima_cuota.fecha_pago_cuota is None:
                        resultados.append(f"La última cuota del cronograma {cronograma.id_cpagos} no tiene fecha de pago")
                    else:
                        resultados.append(f"La última cuota del cronograma {cronograma.id_cpagos} aún no ha pasado")
            else:
                resultados.append(f"El cronograma {cronograma.id_cpagos} no tiene cuotas")

        return Response({"resultados": resultados})


# Función para generar tokens JWT manualmente
def create_jwt_token(persona):
    payload = {
        'id_persona': persona.id_persona,
        'exp': datetime.utcnow() + timedelta(hours=24),  # Token expira en 24 horas
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token




@api_view(['POST'])
def login(request):
    # Obtener el nombre de usuario y la contraseña del request
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Autenticar al usuario
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        try:
            # Obtener los datos del PersonaStaff asociado al usuario
            persona_staff = PersonaStaff.objects.get(user=user)
            
            # Verificar si el PersonaStaff está asociado a una empresa
            empresa = persona_staff.id_empresa if persona_staff.id_empresa else None

            # Crear o obtener el token del usuario
            token, created = Token.objects.get_or_create(user=user)
            
            # Preparar la URL de la foto si existe
            foto_url = (
                request.build_absolute_uri(persona_staff.foto.url)
                if persona_staff.foto
                else None
            )

            # Retornar los datos del usuario junto con los detalles de PersonaStaff y el token
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'persona_staff': {
                    'nombres': persona_staff.nombres,
                    'apellidos': persona_staff.apellidos,
                    'correo': persona_staff.correo,
                    'celular': persona_staff.celular,
                    'rol': persona_staff.rol,
                    'area': persona_staff.area,
                    'dni': persona_staff.dni,
                    'foto': foto_url,  # URL de la foto
                    'empresa': {
                        'nombre_empresa': empresa.nombre_empresa,
                        'ruc': empresa.ruc
                    } if empresa else None
                }
                
            }, status=status.HTTP_200_OK)
        
        except PersonaStaff.DoesNotExist:
            return Response({'error': 'PersonaStaff no asociado a este usuario'}, status=status.HTTP_404_NOT_FOUND)
    
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    

# View del modelo DetallePersona
class DetallePersonaViewSet(viewsets.ModelViewSet):

    queryset = DetallePersona.objects.all()
    serializer_class = DetallePersonaSerializer


# View del modelo Empresa
class EmpresaViewSet(viewsets.ModelViewSet):

    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


# View del modelo PersonaStaff
class PersonaStaffViewSet(viewsets.ModelViewSet):

    queryset = PersonaStaff.objects.all()
    serializer_class = PersonaStaffSerializer

    def get_serializer_context(self):
        # Incluir el request en el contexto
        return {'request': self.request}
    

# View del modelo SeparacionCliente
class SeparacionClienteViewSet(viewsets.ModelViewSet):

    queryset = SeparacionCliente.objects.all()
    serializer_class = PersonaClientSerializer


# View del modelo ObservacionSeparacion
class ObservacionSeparacionViewSet(viewsets.ModelViewSet):

    queryset = ObservacionSeparacion.objects.all()
    serializer_class = ObservacionSeparacionSerializer




@api_view(['POST'])
def request_password_reset(request):
    email = request.data.get('email')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Usuario con este correo no existe.'}, status=status.HTTP_404_NOT_FOUND)

    # Generar un nuevo token de restablecimiento único
    token = get_random_string(length=32)
    
    # Crear o actualizar el token de restablecimiento
    PasswordResetToken.objects.update_or_create(user=user, defaults={'token': token})

    # Enviar el correo con el nuevo enlace de restablecimiento
    reset_url = f'http://localhost:3000/reset-password/{token}'
    send_mail(
        'Restablecer contraseña',
        f'Haga clic en el siguiente enlace para restablecer su contraseña: {reset_url}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )

    return Response({'message': 'Correo enviado con el enlace de restablecimiento.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def validate_password_reset_token(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)

        # Verificar si el token es válido
        if not reset_token.is_valid():
            return Response({'error': 'El token ha expirado. Solicita un nuevo enlace de restablecimiento.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Token válido. Procede a restablecer la contraseña.'}, status=status.HTTP_200_OK)

    except PasswordResetToken.DoesNotExist:
        return Response({'error': 'Token inválido. Solicita un nuevo enlace de restablecimiento.'}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def reset_password(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)

        # Verificar si el token es válido
        if not reset_token.is_valid():
            return Response({'error': 'El token ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({'error': 'Las contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)

        # Actualizar la contraseña del usuario utilizando set_password
        user = reset_token.user
        user.set_password(new_password)
        user.save()

        # Eliminar el token después de su uso
        reset_token.delete()

        return Response({'message': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)

    except PasswordResetToken.DoesNotExist:
        return Response({'error': 'Token inválido.'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def get_lotes_libres(request):
    proyecto_nombre = request.data.get('proyecto_nombre')
    if not proyecto_nombre:
        return Response({'error': 'No se proporcionó el nombre del proyecto.'}, status=400)
    try:
        proyecto = Proyecto.objects.get(nombre_proyecto=proyecto_nombre)
    except Proyecto.DoesNotExist:
        return Response({'error': 'El proyecto no existe.'}, status=404)
    # Obtener los lotes con estado 'LIBRE' en el proyecto especificado
    lotes_libres = Lote.objects.filter(id_proyecto=proyecto, estado='LIBRE')
    # Serializar los lotes
    serializer = LoteSerializer(lotes_libres, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@transaction.atomic
def post_cliente_separacion(request):
    # Extraer datos del request
    data = request.data

    # Obtener el ID del lote seleccionado del request
    lote_id = data.get('lote_id')
    if not lote_id:
        return Response({'error': 'No se proporcionó el ID del lote.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validar los datos del lote seleccionado
    try:
        lote_libre = Lote.objects.get(id_lote=lote_id, estado='LIBRE')
    except Lote.DoesNotExist:
        return Response({'error': 'El lote seleccionado no está disponible o no existe.'}, status=status.HTTP_404_NOT_FOUND)

    # Obtener los campos del cliente y cónyuge con los nombres correctos según el modelo
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    tipo_documento = data.get('tipo_documento')
    num_documento = data.get('num_documento')
    direccion = data.get('direccion')
    email = data.get('correo')
    telefono_fijo = data.get('telefono_fijo')
    celular = data.get('celular')
    inicial_separacion = data.get('inicial_separacion')
    tipo_moneda = data.get('tipo_moneda')
    tiene_conyuge = data.get('conyuge')
    nombre_conyuge = data.get('nombre_conyuge')
    apellidos_conyuge = data.get('apellidos_conyuge')
    dni_conyuge = data.get('dni_conyuge')
    tipo_cliente = data.get('tipo_cliente')
    fecha_separacion = data.get('fecha_separacion', timezone.now())  # Si no se proporciona, usa la fecha actual
    fecha_limite_separacion = data.get('fecha_limite_separacion')  # Nueva fecha límite de separación

    # Generar el código de boleta de separación de forma segura
    try:
        last_ficha = FichaDatosCliente.objects.order_by('-id_fichadc').first()  # Ordenar por el ID para obtener el último registro
        if last_ficha and last_ficha.cod_boleta:
            last_number = int(last_ficha.cod_boleta.split('-')[1])
            new_number = last_number + 1
        else:
            new_number = 1
        
        cod_boleta = f"SO-{new_number:05d}"
    except Exception as e:
        return Response({'error': f'Error al generar el código de boleta: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Validar los datos requeridos del cliente principal
    campos_requeridos = ['nombres', 'apellidos', 'tipo_documento', 'num_documento', 'direccion', 'correo', 'celular', 'inicial_separacion', 'tipo_moneda', 'tipo_cliente']
    campos_faltantes = [campo for campo in campos_requeridos if not data.get(campo)]

    if campos_faltantes:
        return Response({'error': f'Faltan los siguientes campos requeridos: {", ".join(campos_faltantes)}'}, status=status.HTTP_400_BAD_REQUEST)

    # Marcar el lote como reservado
    try:
        lote_libre.estado = 'SEPARADO'
        lote_libre.save()
    except Exception as e:
        return Response({'error': f'Error al reservar el lote: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Crear una instancia de CronogramaPagos
    try:
        cronograma_pagos = CronogramaPagos.objects.create(
            inicial_separacion=inicial_separacion,
            tipo_moneda=tipo_moneda,
        )
    except Exception as e:
        return Response({'error': f'Error al crear el cronograma de pagos: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Crear una instancia de FichaDatosCliente con el código generado, la fecha de separación y la fecha límite de separación
    try:
        ficha_datos_cliente = FichaDatosCliente.objects.create(
            fecha_separacion=fecha_separacion,
            fecha_limite_separacion=fecha_limite_separacion,  # Guardar la fecha límite de separación
            id_cpagos=cronograma_pagos,
            id_lote=lote_libre,
            cod_boleta=cod_boleta
        )
    except Exception as e:
        return Response({'error': f'Error al crear la ficha de datos del cliente: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Crear o recuperar una instancia de PersonaClient para el cliente principal
    try:
        persona_client, created = PersonaClient.objects.get_or_create(
            num_documento=num_documento,
            defaults={
                'nombres': nombres,
                'apellidos': apellidos,
                'correo': email,
                'celular': celular,
                'telefono_fijo': telefono_fijo,
                'tipo_documento': tipo_documento,
                'conyuge': True if tiene_conyuge and tiene_conyuge.lower() == 'si' else False,
                'direccion': direccion,
            }
        )

        # Crear una instancia de DetallePersona para el cliente principal
        DetallePersona.objects.create(
            tipo_cliente=tipo_cliente,
            id_persona_client=persona_client,
            id_fichadc=ficha_datos_cliente,
        )

        # Si hay cónyuge, verificar y crear su información
        if tiene_conyuge and tiene_conyuge.lower() == 'si':
            persona_conyuge, created_conyuge = PersonaClient.objects.get_or_create(
                num_documento=dni_conyuge,
                defaults={
                    'nombres': nombre_conyuge,
                    'apellidos': apellidos_conyuge,
                    'tipo_documento': "DNI",
                    'conyuge': False,
                    'direccion': direccion,
                }
            )

            # Crear una instancia de DetallePersona para el cónyuge
            DetallePersona.objects.create(
                tipo_cliente="CONYUGUE",
                id_persona_client=persona_conyuge,
                id_fichadc=ficha_datos_cliente,
            )
    except Exception as e:
        return Response({'error': f'Error al crear el cliente o cónyuge: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'mensaje': 'Lote reservado y datos del cliente registrados correctamente', 'cod_boleta': cod_boleta}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@transaction.atomic
def post_lote_conyuge(request):
    # Extraer datos del request
    data = request.data

    # Obtener los campos del cliente principal
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    tipo_documento = data.get('tipo_documento')
    num_documento = data.get('num_documento')
    direccion = data.get('direccion')
    email = data.get('correo')
    telefono_fijo = data.get('telefono_fijo')
    celular = data.get('celular')
    inicial_separacion = data.get('inicial_separacion')
    tipo_moneda = data.get('tipo_moneda')
    conyuge = data.get('conyuge')  # Debería ser un booleano
    tipo_cliente = data.get('tipo_cliente')
    cod_boleta = data.get('cod_boleta')  # Código de boleta generado desde otro endpoint

    # Validar que el código de boleta esté presente
    if not cod_boleta:
        return Response({'error': 'No se proporcionó el código de boleta.'}, status=status.HTTP_400_BAD_REQUEST)

    # Validar que 'conyuge' sea True
    if not conyuge:
        return Response({'error': 'Este endpoint solo se utiliza cuando el cliente tiene un cónyuge (conyuge=True).'}, status=status.HTTP_400_BAD_REQUEST)

    # Validar los datos requeridos del cliente principal
    campos_requeridos = ['nombres', 'apellidos', 'tipo_documento', 'num_documento', 'direccion', 'correo', 'celular', 'inicial_separacion', 'tipo_moneda', 'tipo_cliente', 'conyuge', 'cod_boleta']
    campos_faltantes = [campo for campo in campos_requeridos if campo not in data or data.get(campo) in [None, '', False]]

    if campos_faltantes:
        return Response({'error': f'Faltan los siguientes campos requeridos: {", ".join(campos_faltantes)}'}, status=status.HTTP_400_BAD_REQUEST)

    # Validar y obtener datos del cónyuge
    conyuge_nombres = data.get('conyuge_nombres')
    conyuge_apellidos = data.get('conyuge_apellidos')
    conyuge_tipo_documento = data.get('conyuge_tipo_documento')
    conyuge_num_documento = data.get('conyuge_num_documento')

    # Validar datos requeridos del cónyuge
    campos_requeridos_conyuge = ['conyuge_nombres', 'conyuge_apellidos', 'conyuge_tipo_documento', 'conyuge_num_documento']
    campos_faltantes_conyuge = [campo for campo in campos_requeridos_conyuge if not data.get(campo)]
    if campos_faltantes_conyuge:
        return Response({'error': f'Faltan los siguientes campos requeridos del cónyuge: {", ".join(campos_faltantes_conyuge)}'}, status=status.HTTP_400_BAD_REQUEST)

    # 1. Seleccionar un lote libre
    try:
        lote_libre = Lote.objects.filter(estado='LIBRE').first()
        if not lote_libre:
            return Response({'error': 'No hay lotes libres disponibles'}, status=status.HTTP_400_BAD_REQUEST)

        # Marcar el lote como reservado
        lote_libre.estado = 'RESERVADO'
        lote_libre.save()
    except Exception as e:
        return Response({'error': f'Error al seleccionar el lote libre: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 2. Crear una instancia de PersonaClient para el cliente principal
    try:
        persona_client = PersonaClient.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            correo=email,
            celular=celular,
            telefono_fijo=telefono_fijo,
            tipo_documento=tipo_documento,
            num_documento=num_documento,
            conyuge=True,  # Ya que conyuge es True
            direccion=direccion,
        )
    except Exception as e:
        return Response({'error': f'Error al crear el cliente: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 3. Crear una instancia de CronogramaPagos
    try:
        cronograma_pagos = CronogramaPagos.objects.create(
            inicial_separacion=inicial_separacion,
            tipo_moneda=tipo_moneda,
        )
    except Exception as e:
        return Response({'error': f'Error al crear el cronograma de pagos: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 4. Crear una instancia de FichaDatosCliente con el código de boleta recibido
    try:
        ficha_datos_cliente = FichaDatosCliente.objects.create(
            fecha_separacion=timezone.now(),
            id_cpagos=cronograma_pagos,
            id_lote=lote_libre,
            cod_boleta=cod_boleta  # Asignar el código generado desde el otro endpoint
        )
    except Exception as e:
        return Response({'error': f'Error al crear la ficha de datos del cliente: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 5. Crear una instancia de DetallePersona para el cliente principal
    try:
        detalle_persona = DetallePersona.objects.create(
            tipo_cliente=tipo_cliente,
            id_persona_client=persona_client,
            id_fichadc=ficha_datos_cliente,
        )
    except Exception as e:
        return Response({'error': f'Error al crear el detalle de persona: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 6. Crear la instancia de PersonaClient para el cónyuge
    try:
        # Crear la instancia de PersonaClient para el cónyuge
        persona_conyuge = PersonaClient.objects.create(
            nombres=conyuge_nombres,
            apellidos=conyuge_apellidos,
            tipo_documento=conyuge_tipo_documento,
            num_documento=conyuge_num_documento,
            conyuge=False,  # Asumimos que el cónyuge no tiene otro cónyuge
        )

        # Crear la instancia de DetallePersona para el cónyuge
        detalle_persona_conyuge = DetallePersona.objects.create(
            tipo_cliente='CONYUGE',
            id_persona_client=persona_conyuge,
            id_fichadc=ficha_datos_cliente,
        )
    except Exception as e:
        return Response({'error': f'Error al crear los datos del cónyuge: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'mensaje': 'Lote reservado y datos del cliente y cónyuge registrados correctamente', 'cod_boleta': cod_boleta}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def generate_boleta_code(request):
    # Obtener el último código generado de la base de datos
    last_ficha = FichaDatosCliente.objects.order_by('-cod_boleta').first()
    
    if last_ficha and last_ficha.cod_boleta:
        # Extraer el número del último código generado
        last_number = int(last_ficha.cod_boleta.split('-')[1])
        new_number = last_number + 1
    else:
        # Si no hay ningún código previo, empezamos desde 1
        new_number = 1
    
    # Formatear el nuevo número con ceros a la izquierda para que siempre tenga 5 dígitos
    new_code = f"SO-{new_number:05d}"
    
    return Response({'cod_boleta': new_code}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_last_boleta_code(request):
    # Obtener el último código de boleta de la base de datos
    last_ficha = FichaDatosCliente.objects.order_by('-cod_boleta').first()

    # Si hay un código existente, devolverlo, de lo contrario, devolver un código por defecto
    last_code = last_ficha.cod_boleta if last_ficha and last_ficha.cod_boleta else "SO-00000"

    return Response({'last_code': last_code}, status=status.HTTP_200_OK)


@api_view(['POST'])
def crear_cuotas(request):
    try:
        # Obtener los datos del request
        id_cpagos = request.data.get('id_cpagos')
        cronograma = CronogramaPagos.objects.get(id_cpagos=id_cpagos)

        # Validar que el cronograma tiene la fecha de pago de cuota
        if not cronograma.fecha_pago_cuota:
            return Response(
                {'error': 'El cronograma no tiene definida la fecha de pago de cuota.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verificar si ya existen cuotas asociadas a este cronograma y eliminarlas
        Cuota.objects.filter(id_cpagos=cronograma).delete()

        # Verificar si el cliente ya pagó todas las cuotas
        if cronograma.numero_cuotas == cronograma.numero_cuotas_pagadas:
            # Crear todas las cuotas con estado 'False' ya que el cliente pagó todo
            cuotas_creadas = []
            
            # Validar si existen los montos en soles, de lo contrario convertir desde dólares
            if cronograma.precio_venta_soles is None or cronograma.cuota_inicial_soles is None:
                if cronograma.precio_venta_dolares and cronograma.cuota_inicial_dolares and cronograma.tipo_cambio:
                    # Convertir dólares a soles
                    precio_venta_soles = cronograma.precio_venta_dolares * cronograma.tipo_cambio
                    cuota_inicial_soles = cronograma.cuota_inicial_dolares * cronograma.tipo_cambio
                else:
                    return Response(
                        {'error': 'Faltan valores en soles y dólares o el tipo de cambio.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                precio_venta_soles = cronograma.precio_venta_soles
                cuota_inicial_soles = cronograma.cuota_inicial_soles

            # Calcular el monto de cada cuota
            monto_cuota = (precio_venta_soles - cuota_inicial_soles) / cronograma.numero_cuotas

            # Si hay fecha_pago_cuota, siempre crear las cuotas con las fechas, reduciendo un mes por cada una
            fecha_actual = cronograma.fecha_pago_cuota
            dia_original = fecha_actual.day

            for i in range(cronograma.numero_cuotas):
                try:
                    fecha_cuota = fecha_actual.replace(day=dia_original)
                except ValueError:
                    fecha_cuota = fecha_actual + relativedelta(day=31)

                # Crear la cuota con fecha y estado 'False'
                cuota = Cuota.objects.create(
                    fecha_pago_cuota=fecha_cuota,
                    monto_cuota=monto_cuota,
                    id_cpagos=cronograma,
                    pago_adelantado=False,
                    estado=False,  # El cliente ya pagó todo, no hay cuotas morosas
                    tipo_moneda='SOLES'
                )
                cuotas_creadas.append(cuota.id_cuota)

                # Restar un mes para la siguiente cuota
                fecha_actual -= relativedelta(months=1)

            return Response(
                {
                    'mensaje': f'Todas las cuotas ({len(cuotas_creadas)}) creadas con estado False (ya pagadas).',
                    'cuotas': cuotas_creadas
                },
                status=status.HTTP_201_CREATED
            )

        # Si no ha pagado ninguna cuota (numero_cuotas_pagadas == 0), crear una cuota morosa con estado=True
        if cronograma.numero_cuotas_pagadas == 0:
            if cronograma.precio_venta_soles and cronograma.cuota_inicial_soles:
                monto_cuota = (
                    (cronograma.precio_venta_soles - cronograma.cuota_inicial_soles) / 
                    cronograma.numero_cuotas
                )
            else:
                # Validar si existen los montos en soles, de lo contrario convertir desde dólares
                if cronograma.precio_venta_soles is None or cronograma.cuota_inicial_soles is None:
                    if cronograma.precio_venta_dolares and cronograma.cuota_inicial_dolares and cronograma.tipo_cambio:
                        # Convertir dólares a soles
                        precio_venta_soles = cronograma.precio_venta_dolares * cronograma.tipo_cambio
                        cuota_inicial_soles = cronograma.cuota_inicial_dolares * cronograma.tipo_cambio
                    else:
                        return Response(
                            {'error': 'Faltan valores en soles y dólares o el tipo de cambio.'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    precio_venta_soles = cronograma.precio_venta_soles
                    cuota_inicial_soles = cronograma.cuota_inicial_soles

                monto_cuota = (precio_venta_soles - cuota_inicial_soles) / cronograma.numero_cuotas

            # Crear una única cuota morosa con estado=True
            cuota = Cuota.objects.create(
                fecha_pago_cuota=cronograma.fecha_pago_cuota,
                monto_cuota=monto_cuota,
                id_cpagos=cronograma,
                pago_adelantado=False,
                estado=True,  # Moroso
                tipo_moneda='SOLES'
            )

            return Response(
                {
                    'mensaje': '1 cuota creada con estado moroso.',
                    'cuotas': [cuota.id_cuota]
                },
                status=status.HTTP_201_CREATED
            )

        # Continuar con el proceso normal si no ha pagado todas las cuotas
        if (
            cronograma.numero_cuotas_pagadas and 
            cronograma.precio_venta_soles and 
            cronograma.cuota_inicial_soles
        ):
            monto_cuota = (
                (cronograma.precio_venta_soles - cronograma.cuota_inicial_soles) / 
                cronograma.numero_cuotas
            )
        else:
            # Validar si existen los montos en soles, de lo contrario convertir desde dólares
            if cronograma.precio_venta_soles is None or cronograma.cuota_inicial_soles is None:
                if cronograma.precio_venta_dolares and cronograma.cuota_inicial_dolares and cronograma.tipo_cambio:
                    # Convertir dólares a soles
                    precio_venta_soles = cronograma.precio_venta_dolares * cronograma.tipo_cambio
                    cuota_inicial_soles = cronograma.cuota_inicial_dolares * cronograma.tipo_cambio
                else:
                    return Response(
                        {'error': 'Faltan valores en soles y dólares o el tipo de cambio.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                precio_venta_soles = cronograma.precio_venta_soles
                cuota_inicial_soles = cronograma.cuota_inicial_soles

            monto_cuota = (precio_venta_soles - cuota_inicial_soles) / cronograma.numero_cuotas

            
        # Crear las cuotas morosas y no morosas
        cuotas_creadas = []
        fecha_actual = cronograma.fecha_pago_cuota
        dia_original = fecha_actual.day

        for i in range(cronograma.numero_cuotas_pagadas):
            try:
                fecha_cuota = fecha_actual.replace(day=dia_original)
            except ValueError:
                fecha_cuota = fecha_actual + relativedelta(day=31)

            cuota = Cuota.objects.create(
                fecha_pago_cuota=fecha_cuota,
                monto_cuota=monto_cuota,
                id_cpagos=cronograma,
                pago_adelantado=False,
                estado=True if i == 0 else False,  # La primera cuota es morosa
                tipo_moneda='SOLES'
            )
            cuotas_creadas.append(cuota.id_cuota)
            fecha_actual -= relativedelta(months=1)

        return Response(
            {
                'mensaje': f'{len(cuotas_creadas)} cuotas creadas con éxito.',
                'cuotas': cuotas_creadas
            },
            status=status.HTTP_201_CREATED
        )

    except CronogramaPagos.DoesNotExist:
        return Response(
            {'error': 'Cronograma de pagos no encontrado.'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': f'Ocurrió un error: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )