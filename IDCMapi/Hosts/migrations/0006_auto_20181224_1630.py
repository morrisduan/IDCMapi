# Generated by Django 2.1.4 on 2018-12-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0005_auto_20181224_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='network_adapters',
            field=models.PositiveSmallIntegerField(blank=True, db_column='network_adapters', null=True),
        ),
    ]
