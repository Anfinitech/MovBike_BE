# Generated by Django 3.2.7 on 2021-10-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoveAndFlowApp', '0003_alter_bicicleta_b_en_estacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='b_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
