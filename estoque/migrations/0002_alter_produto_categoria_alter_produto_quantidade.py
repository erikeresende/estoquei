# Generated by Django 5.1 on 2024-08-25 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
    ]
