# Generated by Django 2.2 on 2021-12-20 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20211220_0803'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Eventer',
        ),
    ]