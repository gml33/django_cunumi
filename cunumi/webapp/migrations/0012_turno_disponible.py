# Generated by Django 4.2.1 on 2024-01-30 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_historiaclinica_paciente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='disponible',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
