# Generated by Django 5.0.6 on 2024-05-22 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_delete_programmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='colindacia_derecha',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='colindacia_fondo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='colindacia_frente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='colindacia_izquierda',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='distancia_derecha',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='distancia_fondo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='distancia_frente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='distancia_izquierda',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='ip_estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.estado'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='ip_manzana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.manzana'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='numero_lote',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='perimetro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='precio_m2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
