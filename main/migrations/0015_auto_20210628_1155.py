# Generated by Django 3.2.4 on 2021-06-28 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0014_auto_20210628_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_cart',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='goods_cart',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]