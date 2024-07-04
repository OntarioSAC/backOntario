# signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import FichaDatosCliente, CronogramaPagos

@receiver(post_delete, sender=FichaDatosCliente)
def make_cronograma_pagos_available(sender, instance, **kwargs):
    # Si un cronograma de pagos estaba asignado a esta ficha,
    # debe volver a estar disponible para ser asignado nuevamente
    if instance.id_cpagos:
        instance.id_cpagos.save()
