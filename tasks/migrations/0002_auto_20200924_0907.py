# Generated by Django 3.1.1 on 2020-09-24 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='status',
            new_name='complete',
        ),
    ]
