# Generated by Django 5.0.6 on 2024-05-20 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_persona_id_cliente_cerrado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientecerrado',
            name='id_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.persona'),
        ),
    ]
