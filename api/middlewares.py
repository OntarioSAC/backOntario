from datetime import date, timedelta
from django.utils.deprecation import MiddlewareMixin
from .models import CronogramaPagos, Cuota

class VerificarCuotasMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Obtener todos los cronogramas de pagos
        cronogramas = CronogramaPagos.objects.all()

        for cronograma in cronogramas:
            # Obtener la última cuota del cronograma
            ultima_cuota = Cuota.objects.filter(id_cpagos=cronograma).order_by('-fecha_pago_cuota').first()

            if ultima_cuota and ultima_cuota.fecha_pago_cuota and ultima_cuota.fecha_pago_cuota < date.today():
                # Si ha pasado, crear una nueva cuota 30 días después de la última
                nueva_fecha_pago_cuota = ultima_cuota.fecha_pago_cuota + timedelta(days=30)

                # Verificar si no excede el número de cuotas
                cuotas_existentes = Cuota.objects.filter(id_cpagos=cronograma).count()
                if cuotas_existentes < cronograma.numero_cuotas:
                    nueva_cuota = Cuota(
                        fecha_pago_cuota=nueva_fecha_pago_cuota,
                        id_cpagos=cronograma,
                        monto_cuota=ultima_cuota.monto_cuota,
                        estado=True,
                        tipo_moneda=ultima_cuota.tipo_moneda
                    )
                    nueva_cuota.save()
        # El middleware no interfiere con la respuesta, así que continúa normalmente
        return None
