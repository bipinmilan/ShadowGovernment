# Generated by Django 2.1.7 on 2020-02-11 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0054_auto_20200209_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='related_ministry',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='offices.ExecutiveOffice'),
        ),
    ]
