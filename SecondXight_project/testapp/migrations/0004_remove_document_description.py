# Generated by Django 3.0.3 on 2020-02-29 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20200229_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]