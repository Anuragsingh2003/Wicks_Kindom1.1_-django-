# Generated by Django 4.1.7 on 2023-02-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wicksapp', '0002_rename_weapon_name_adminusr_admin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminusr',
            name='weapon_img',
            field=models.ImageField(blank=True, null=True, upload_to='admin_conf/'),
        ),
        migrations.AlterField(
            model_name='armorydata',
            name='weapon_img',
            field=models.ImageField(blank=True, null=True, upload_to='admin_conf/'),
        ),
    ]
