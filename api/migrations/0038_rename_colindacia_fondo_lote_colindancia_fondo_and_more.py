# Generated by Django 5.0.6 on 2024-05-27 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_remove_proyecto_id_manzana_manzana_id_proyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='colindacia_fondo',
            new_name='colindancia_fondo',
        ),
        migrations.RenameField(
            model_name='lote',
            old_name='colindacia_izquierda',
            new_name='colindancia_izquierda',
        ),
    ]
