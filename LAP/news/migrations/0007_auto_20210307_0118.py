# Generated by Django 3.1.5 on 2021-03-06 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210307_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(max_length=12),
        ),
    ]