# Generated by Django 4.2.13 on 2024-09-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_alter_cuota_morosidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuota',
            name='estado',
        ),
        migrations.AlterField(
            model_name='cuota',
            name='morosidad',
            field=models.BooleanField(default=False),
        ),
    ]