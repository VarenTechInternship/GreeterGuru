# Generated by Django 2.2.2 on 2019-06-19 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0025_auto_20190619_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='pic_name',
            new_name='name',
        ),
    ]