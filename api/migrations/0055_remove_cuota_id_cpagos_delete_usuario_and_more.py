# Generated by Django 4.2.13 on 2024-09-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_rename_cuota_balloon_cronogramapagos_precio_venta_dolares_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuota',
            name='id_cpagos',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RenameField(
            model_name='cronogramapagos',
            old_name='descripcion_cpagos',
            new_name='observaciones',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='fecha_registro',
            new_name='area',
        ),
        migrations.RemoveField(
            model_name='cronogramapagos',
            name='cuota_mensual',
        ),
        migrations.RemoveField(
            model_name='cronogramapagos',
            name='dias_pago',
        ),
        migrations.RemoveField(
            model_name='cronogramapagos',
            name='plazo_anios',
        ),
        migrations.RemoveField(
            model_name='cronogramapagos',
            name='plazo_meses',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='antiguedad_laboral',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='constancia_inicial',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_area',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_canal',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_documento',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_medio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_origen',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id_rol',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='profesion',
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='amortizacion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='deuda_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='fecha_pago_cuota',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='numero_cuotas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='numero_cuotas_pagadas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cronogramapagos',
            name='tipo_cambio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='canal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_creacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='medio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='num_documento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='origen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_documento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramapagos',
            name='TEA',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramapagos',
            name='cuota_inicial',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramapagos',
            name='descuento',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramapagos',
            name='fecha_inicio_pago',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Canal',
        ),
        migrations.DeleteModel(
            name='Cuota',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
        migrations.DeleteModel(
            name='Medio',
        ),
        migrations.DeleteModel(
            name='Origen',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
