# Generated by Django 3.2.7 on 2021-10-31 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoveAndFlowApp', '0012_alter_prestamo_p_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='b_en_prestamo',
            field=models.BooleanField(default=False, null=True),
        ),
    ]