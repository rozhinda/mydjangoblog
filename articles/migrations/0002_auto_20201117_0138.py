# Generated by Django 3.1.3 on 2020-11-16 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tittle',
            new_name='title',
        ),
    ]
