# Generated by Django 5.1.3 on 2024-11-26 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0003_alter_assetkpi_asset_id_alter_assetkpi_kpi_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetkpi',
            name='asset_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assetkpi',
            name='kpi_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='kpi.kpi'),
        ),
    ]