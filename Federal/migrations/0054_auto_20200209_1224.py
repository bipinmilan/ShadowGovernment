# Generated by Django 2.1.7 on 2020-02-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0053_auto_20200209_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='judiciary',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='legislative',
            name='description',
            field=models.TextField(default=False),
        ),
    ]
