# Generated by Django 3.2.7 on 2021-09-25 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210923_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='nome',
            new_name='texto',
        ),
    ]