# Generated by Django 3.1.1 on 2020-09-28 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='netflix',
            old_name='line',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='netflix',
            old_name='plot',
            new_name='series',
        ),
        migrations.RenameField(
            model_name='netflix',
            old_name='character',
            new_name='user',
        ),
    ]
