# Generated by Django 4.2.1 on 2023-06-04 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_derivacion_profesional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='numero',
            new_name='identificador',
        ),
    ]
