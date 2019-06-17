# Generated by Django 2.0.13 on 2019-06-19 18:17

from django.db import migrations, models
import django.db.models.deletion
import workflow.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_email', models.EmailField(default='', max_length=254)),
                ('admin_permissions', models.CharField(choices=[(0, 'User'), (1, 'Superuser'), (2, 'Superadmin')], default=0, max_length=15)),
                ('is_two_factor', models.BooleanField(default=False, verbose_name='Two-Factor Authentication')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=30)),
                ('emp_ID', models.IntegerField(default=0)),
                ('emp_email', models.EmailField(default='', max_length=254)),
                ('emp_permissions', models.CharField(choices=[(0, 'Never'), (1, 'Sometimes'), (2, 'Always')], default=0, max_length=15)),
                ('manager_email', models.EmailField(default='', max_length=254)),
                ('key_code', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_photo', models.ImageField(upload_to='')),
                ('photos', models.FileField(upload_to=workflow.models.Photo.user_directory_path)),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='workflow.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Photo',
            fields=[
                ('temp_id', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('unknown_photo', models.FileField(upload_to=workflow.models.Temp_Photo.temp_path)),
            ],
        ),
    ]
