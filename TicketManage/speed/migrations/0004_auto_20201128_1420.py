# Generated by Django 3.1.3 on 2020-11-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('speed', '0003_auto_20201128_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
