# Generated by Django 3.0.4 on 2020-03-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identificaciones', '0002_auto_20200309_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identificacion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='identificacion',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
