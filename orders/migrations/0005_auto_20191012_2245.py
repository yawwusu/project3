# Generated by Django 2.0.3 on 2019-10-12 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191012_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='fooditem',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='size',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
