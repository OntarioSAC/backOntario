# Generated by Django 4.2.13 on 2024-08-29 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_remove_manzana_id_proyecto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='fecha_fin',
        ),
    ]