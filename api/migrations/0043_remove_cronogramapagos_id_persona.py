# Generated by Django 5.0.6 on 2024-07-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_alter_cronogramapagos_cuota_balloon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronogramapagos',
            name='id_persona',
        ),
    ]
