# Generated by Django 5.2 on 2025-06-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
            ],
        ),
    ]
