# Generated by Django 3.0.7 on 2020-07-20 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='articlerevision',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='component',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='componentversion',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='cvedatafile',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='review',
            name='data_source',
        ),
    ]