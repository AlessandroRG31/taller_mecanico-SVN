# mantenimiento/migrations/0003_fix_cliente_field.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0002_vehiculo_fecha_proxima_revision_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cliente',
            field=models.ForeignKey(
                default=1,  # Ajusta este ID si no existe ese cliente
                on_delete=models.CASCADE,
                related_name='vehiculos',
                to='clientes.cliente',
                verbose_name='Cliente',
            ),
            preserve_default=False,
        ),
    ]
