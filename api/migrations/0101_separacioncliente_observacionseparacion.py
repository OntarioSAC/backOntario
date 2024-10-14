# Generated by Django 4.2.13 on 2024-10-11 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0100_fichadatoscliente_fecha_limite_separacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeparacionCliente',
            fields=[
                ('id_separacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_separacion', models.DateField(default=django.utils.timezone.now)),
                ('fecha_limite_separacion', models.DateField(blank=True, null=True)),
                ('monto_separacion', models.FloatField(blank=True, null=True)),
                ('estado_separacion', models.CharField(choices=[('ACTIVO', 'Activo'), ('CANCELADO', 'Cancelado')], default='ACTIVO', max_length=20)),
                ('id_fichadc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.fichadatoscliente')),
            ],
        ),
        migrations.CreateModel(
            name='ObservacionSeparacion',
            fields=[
                ('id_observacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('id_separacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.separacioncliente')),
            ],
        ),
    ]
