# Generated by Django 5.0.6 on 2024-05-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_personaproyecto_id_cpagos'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_registro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
