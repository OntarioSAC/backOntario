# Generated by Django 4.2.13 on 2024-09-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_alter_lote_colindancia_derecha_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='precio_m2',
            new_name='precio_m2_dolares',
        ),
        migrations.AddField(
            model_name='lote',
            name='precio_m2_soles',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]