# Generated by Django 2.2.5 on 2021-06-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='totalPagar',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]
