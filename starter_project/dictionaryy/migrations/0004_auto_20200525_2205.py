# Generated by Django 2.2.1 on 2020-05-26 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaryy', '0003_dictionary_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='userS',
            new_name='user',
        ),
    ]
