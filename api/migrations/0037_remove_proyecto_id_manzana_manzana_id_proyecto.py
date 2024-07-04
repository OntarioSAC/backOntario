# Generated by Django 5.0.6 on 2024-05-24 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_proyecto_id_manzana_delete_proyectomanzana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='id_manzana',
        ),
        migrations.AddField(
            model_name='manzana',
            name='id_proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.proyecto'),
        ),
    ]
