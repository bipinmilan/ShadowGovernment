# Generated by Django 2.1.7 on 2020-02-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0027_auto_20200211_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincejudiciary',
            name='court',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='offices.ProvinceJudiciaryOffice'),
        ),
    ]