# Generated by Django 4.2.13 on 2024-10-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0096_rename_id_persona_observaciones_id_persona_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaclient',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
