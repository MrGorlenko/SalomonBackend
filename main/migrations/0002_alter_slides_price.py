# Generated by Django 3.2.4 on 2021-06-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slides',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
    ]