# Generated by Django 4.2.13 on 2024-10-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0101_separacioncliente_observacionseparacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='personastaff',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='personas/'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='proyectos/'),
        ),
    ]
