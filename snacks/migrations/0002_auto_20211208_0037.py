# Generated by Django 3.2.9 on 2021-12-08 00:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snacks',
            new_name='Snack',
        ),
        migrations.RenameField(
            model_name='snack',
            old_name='descripiton',
            new_name='description',
        ),
    ]
