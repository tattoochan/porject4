# Generated by Django 2.0.2 on 2020-04-19 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_detail',
            old_name='name',
            new_name='position',
        ),
    ]
