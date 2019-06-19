# Generated by Django 2.2.2 on 2019-06-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0014_auto_20190618_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_ID',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='keycode',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(null=True, upload_to='Dataset'),
        ),
    ]