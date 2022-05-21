# Generated by Django 3.2 on 2022-05-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20220518_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('solicitado', 'Solicitado'), ('pagado', 'Pagado')], default='solicitado', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nro_recibo',
            field=models.CharField(default='', max_length=200),
        ),
    ]