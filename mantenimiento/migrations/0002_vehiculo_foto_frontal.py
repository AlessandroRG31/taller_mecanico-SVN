# Generated by Django 5.2 on 2025-06-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='foto_frontal',
            field=models.ImageField(blank=True, null=True, upload_to='vehiculos/', verbose_name='Foto frontal (alternativa)'),
        ),
    ]
