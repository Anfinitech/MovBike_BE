# Generated by Django 3.2.7 on 2021-10-31 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MoveAndFlowApp', '0008_auto_20211014_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='b_en_estacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contiene', to='MoveAndFlowApp.estacion'),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='b_en_prestamo',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_inicio', models.DateTimeField()),
                ('p_fin', models.DateTimeField()),
                ('p_bicicleta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presta', to='MoveAndFlowApp.bicicleta')),
                ('p_destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='llega', to='MoveAndFlowApp.estacion')),
                ('p_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parte', to='MoveAndFlowApp.estacion')),
            ],
        ),
    ]