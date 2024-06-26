# Generated by Django 5.0.6 on 2024-05-21 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_area_descripcion_area'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='permisoarea',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='area',
            name='permisos',
            field=models.ManyToManyField(related_name='areas', through='api.PermisoArea', to='api.permiso'),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='descripcion_permiso',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='permisoarea',
            name='id_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.area'),
        ),
        migrations.AlterField(
            model_name='permisoarea',
            name='id_permiso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.permiso'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
