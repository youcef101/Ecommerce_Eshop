# Generated by Django 3.1.6 on 2021-02-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discountPercentage',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
