# Generated by Django 3.1.6 on 2021-02-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210214_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discountPercentage',
            field=models.IntegerField(default=None),
        ),
    ]
