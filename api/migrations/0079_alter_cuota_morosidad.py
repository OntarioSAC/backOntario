# Generated by Django 4.2.13 on 2024-09-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0078_rename_precio_m2_lote_precio_m2_dolares_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='morosidad',
            field=models.CharField(blank=True, null=True),
        ),
    ]