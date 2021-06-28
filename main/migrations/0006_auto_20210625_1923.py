# Generated by Django 3.2.4 on 2021-06-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210624_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Goods_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='main.cart', verbose_name='Корзина')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.good', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='main.Goods_Cart'),
        ),
    ]
