# Generated by Django 3.1.7 on 2021-07-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210720_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='predicitions',
            new_name='predictions',
        ),
    ]
