# Generated by Django 4.2.2 on 2023-06-29 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carros',
            old_name='Marca',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='carros',
            old_name='Modelo',
            new_name='modelo',
        ),
    ]
