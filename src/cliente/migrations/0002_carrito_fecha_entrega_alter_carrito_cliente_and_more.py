# Generated by Django 5.1.4 on 2024-12-09 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carritos', to='cliente.cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.PositiveIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
