# Generated by Django 3.1.4 on 2020-12-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed', '0007_customer_purchasehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='sometips',
            name='aritcle',
            field=models.CharField(default='This is some describe', max_length=1000),
        ),
    ]
