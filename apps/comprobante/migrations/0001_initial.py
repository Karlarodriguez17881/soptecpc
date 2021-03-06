# Generated by Django 2.2.5 on 2021-06-05 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0004_remove_cliente_direccion'),
        ('pedido', '0005_pedido_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('imagen', models.ImageField(null=True, upload_to='img/comprobante')),
                ('estado', models.CharField(blank=True, default='1', max_length=2, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('id_pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido')),
            ],
        ),
    ]
