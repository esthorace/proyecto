# Generated by Django 5.1 on 2024-08-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
