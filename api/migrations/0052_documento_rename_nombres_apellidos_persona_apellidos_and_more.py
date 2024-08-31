# Generated by Django 4.2.13 on 2024-08-31 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_rename_proyecto_lote_id_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_documento', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='nombres_apellidos',
            new_name='apellidos',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='proyectos',
        ),
        migrations.AddField(
            model_name='persona',
            name='nombres',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='id_documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.documento'),
        ),
    ]
