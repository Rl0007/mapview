# Generated by Django 4.0.5 on 2022-06-17 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_rename_wkb_geometry_admin1_us_wkb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin1_us',
            new_name='admin1',
        ),
        migrations.RenameField(
            model_name='admin1',
            old_name='wkb',
            new_name='wkb_geometry',
        ),
    ]
