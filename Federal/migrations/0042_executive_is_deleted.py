# Generated by Django 2.1.7 on 2019-12-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0041_auto_20191220_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='executive',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
