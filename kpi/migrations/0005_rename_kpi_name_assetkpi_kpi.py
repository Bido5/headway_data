# Generated by Django 5.1.3 on 2024-11-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0004_alter_assetkpi_asset_id_alter_assetkpi_kpi_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetkpi',
            old_name='kpi_name',
            new_name='kpi',
        ),
    ]
