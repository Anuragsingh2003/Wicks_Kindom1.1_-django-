# Generated by Django 4.1.7 on 2023-02-24 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField(auto_created=True, null=True)),
                ('weapon_name', models.CharField(max_length=50)),
                ('weapon_desc', models.TextField()),
                ('weapon_img', models.ImageField(upload_to='admin_conf/')),
            ],
        ),
        migrations.CreateModel(
            name='ArmoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField(auto_created=True, null=True)),
                ('weapon_name', models.CharField(max_length=50)),
                ('weapon_desc', models.TextField()),
                ('url', models.URLField()),
                ('weapon_img', models.ImageField(upload_to='admin_conf/')),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wicksapp.adminusr')),
            ],
        ),
    ]