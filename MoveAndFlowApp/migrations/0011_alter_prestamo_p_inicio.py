# Generated by Django 3.2.7 on 2021-11-01 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoveAndFlowApp', '0010_alter_bicicleta_b_en_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='p_inicio',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
