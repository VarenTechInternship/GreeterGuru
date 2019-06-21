# Generated by Django 2.2.2 on 2019-06-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_auto_20190621_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tempphoto',
            name='name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]