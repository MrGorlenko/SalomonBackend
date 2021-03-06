# Generated by Django 3.2.5 on 2021-07-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210712_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя заказчика')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('rating', models.FloatField(blank=True, default=1, null=True, verbose_name='Популярность')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название товара')),
            ],
            options={
                'verbose_name': 'Комментарии к заказам',
                'verbose_name_plural': 'Комментарии к заказам',
            },
        ),
    ]
