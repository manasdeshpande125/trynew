# Generated by Django 3.2.8 on 2021-10-24 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='desc',
            new_name='msg',
        ),
    ]