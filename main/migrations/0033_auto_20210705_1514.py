# Generated by Django 3.2.4 on 2021-07-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_merge_0029_auto_20210705_0936_0031_auto_20210703_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_cart',
            name='height',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='goods_cart',
            name='size',
            field=models.CharField(blank=True, max_length=50, verbose_name='Размер'),
        ),
    ]
