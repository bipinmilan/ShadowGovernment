# Generated by Django 2.1.7 on 2020-02-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0061_auto_20200211_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='judiciary',
            old_name='related_court',
            new_name='court',
        ),
    ]
