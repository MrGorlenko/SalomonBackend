# Generated by Django 3.2.4 on 2021-06-26 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_good_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='image',
        ),
    ]