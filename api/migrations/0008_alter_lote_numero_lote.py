# Generated by Django 5.0.6 on 2024-05-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_manzana_id_lote_remove_proyecto_id_manzana_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='numero_lote',
            field=models.CharField(max_length=50),
        ),
    ]
