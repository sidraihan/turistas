# Generated by Django 2.2.6 on 2020-03-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistas_rec', '0003_auto_20200225_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(default='nil', max_length=1000),
        ),
        migrations.AlterField(
            model_name='place',
            name='view',
            field=models.CharField(default='nil', max_length=1000),
        ),
    ]
