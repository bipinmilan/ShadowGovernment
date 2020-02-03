# Generated by Django 2.1.7 on 2019-12-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0004_auto_20191227_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='jptmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='provincejudiciary',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='provincejudiciary',
            name='is_deleted',
        ),
    ]
