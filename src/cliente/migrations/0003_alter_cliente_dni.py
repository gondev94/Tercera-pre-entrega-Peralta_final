# Generated by Django 5.1.4 on 2024-12-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_carrito_fecha_entrega_alter_carrito_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.PositiveIntegerField(),
        ),
    ]
