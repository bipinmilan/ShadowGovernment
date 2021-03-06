# Generated by Django 2.1.7 on 2020-02-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0056_auto_20200211_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='judiciary',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='legislative',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category'),
        ),
    ]
