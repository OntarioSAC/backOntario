# Generated by Django 4.2.13 on 2024-08-31 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_documento_rename_nombres_apellidos_persona_apellidos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichadatoscliente',
            name='id_proyecto',
        ),
    ]
