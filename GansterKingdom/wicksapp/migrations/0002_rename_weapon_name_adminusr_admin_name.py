# Generated by Django 4.1.7 on 2023-02-25 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wicksapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminusr',
            old_name='weapon_name',
            new_name='Admin_name',
        ),
    ]
