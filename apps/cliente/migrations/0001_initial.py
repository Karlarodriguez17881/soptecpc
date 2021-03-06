# Generated by Django 2.2.5 on 2021-06-02 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.TextField(blank=True, max_length=10, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cedula', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=150, null=True)),
                ('id_cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
