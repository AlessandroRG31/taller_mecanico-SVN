# mantenimiento/migrations/0004_repuestomantenimiento_alter_mantenimiento_repuestos.py
from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0003_alter_vehiculo_foto_frente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepuestoMantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(
                    default=1,
                    validators=[django.core.validators.MinValueValidator(1)],
                    verbose_name='Cantidad'
                )),
                ('mantenimiento', models.ForeignKey(on_delete=models.CASCADE, to='mantenimiento.Mantenimiento')),
                ('repuesto', models.ForeignKey(on_delete=models.CASCADE, to='repuestos.Repuesto')),
            ],
        ),
        # AlterField comentado intencionalmente para evitar conflicto M2M con through
        # migrations.AlterField(
        #     model_name='mantenimiento',
        #     name='repuestos',
        #     field=models.ManyToManyField(blank=True, related_name='mantenimientos', through='mantenimiento.RepuestoMantenimiento', to='repuestos.Repuesto'),
        # ),
    ]
