# Generated by Django 5.0.6 on 2024-05-20 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_lote_numero_lote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lado',
            name='id_colindancia',
        ),
        migrations.RemoveField(
            model_name='lado',
            name='id_distancia',
        ),
        migrations.RemoveField(
            model_name='perimetro',
            name='id_lado',
        ),
        migrations.AlterUniqueTogether(
            name='loteperimetro',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='loteperimetro',
            name='id_lote',
        ),
        migrations.RemoveField(
            model_name='loteperimetro',
            name='id_perimetro',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='ip_perimetro',
        ),
        migrations.DeleteModel(
            name='Colindancia',
        ),
        migrations.DeleteModel(
            name='Distancia',
        ),
        migrations.DeleteModel(
            name='Lado',
        ),
        migrations.DeleteModel(
            name='LotePerimetro',
        ),
        migrations.DeleteModel(
            name='Perimetro',
        ),
    ]
