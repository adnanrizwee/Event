# Generated by Django 2.2 on 2021-12-20 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='state',
            new_name='gender',
        ),
    ]
