# Generated by Django 3.1.6 on 2021-03-18 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_contact_subscribe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={},
        ),
        migrations.RenameField(
            model_name='subscribe',
            old_name='email',
            new_name='mail',
        ),
    ]
