# Generated by Django 3.1.5 on 2021-02-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210225_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='set_name',
            field=models.TextField(default='-'),
        ),
    ]
