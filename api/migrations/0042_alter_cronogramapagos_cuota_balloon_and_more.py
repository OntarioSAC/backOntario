# Generated by Django 5.0.6 on 2024-07-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_cronogramapagos_cuota_balloon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronogramapagos',
            name='cuota_balloon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramapagos',
            name='cuota_balloon_meses',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]