# Generated by Django 2.0.3 on 2019-10-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ManyToManyField(blank=True, related_name='orders', to='orders.Menu')),
            ],
        ),
    ]
