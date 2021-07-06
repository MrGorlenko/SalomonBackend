# Generated by Django 3.2.4 on 2021-07-06 12:15

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_customer_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
