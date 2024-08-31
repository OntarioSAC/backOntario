# Generated by Django 4.2.13 on 2024-08-29 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_alter_area_nombre_area_alter_persona_correo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manzana',
            name='id_proyecto',
        ),
        migrations.RenameField(
            model_name='lote',
            old_name='numero_lote',
            new_name='estado',
        ),
        migrations.RemoveField(
            model_name='fichadatoscliente',
            name='id_manzana',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='id_estado',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='id_manzana',
        ),
        migrations.AddField(
            model_name='lote',
            name='id_proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.proyecto'),
        ),
        migrations.AddField(
            model_name='lote',
            name='manzana_lote',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Manzana',
        ),
    ]
