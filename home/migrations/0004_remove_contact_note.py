# Generated by Django 3.1.6 on 2021-02-20 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_faq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
    ]
