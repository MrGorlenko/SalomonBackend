# Generated by Django 3.2.5 on 2021-07-10 14:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0005_auto_20210624_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0, verbose_name='Количество товара')),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Итоговая цена')),
                ('in_order', models.BooleanField(default=False, verbose_name='Занятая корзина')),
                ('for_anonymous_users', models.BooleanField(default=False, verbose_name='Для анонимов')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Старая цена')),
                ('sale', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
            },
        ),
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
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.GenericIPAddressField(null=True, verbose_name='IP пользователя')),
            ],
            options={
                'verbose_name': 'IP пользователя товара',
                'verbose_name_plural': 'IP пользователя товара',
            },
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товар'},
        ),
        migrations.AlterModelOptions(
            name='goods_height',
            options={'verbose_name': 'Высота товара', 'verbose_name_plural': 'Высота товара'},
        ),
        migrations.AlterModelOptions(
            name='goods_icons',
            options={'verbose_name': 'Иконка товара', 'verbose_name_plural': 'Товара товара'},
        ),
        migrations.AlterModelOptions(
            name='goods_images',
            options={'verbose_name': 'Картинка товара', 'verbose_name_plural': 'Картинка товара'},
        ),
        migrations.AlterModelOptions(
            name='goods_sizes',
            options={'verbose_name': 'Размер товара', 'verbose_name_plural': 'Размер товара'},
        ),
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'verbose_name': 'Категории товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='slides',
            options={'verbose_name': 'Слайдеры', 'verbose_name_plural': 'Слайдеры'},
        ),
        migrations.AddField(
            model_name='good',
            name='ability_to_twist',
            field=models.BooleanField(default=False, verbose_name='Возможность скрутить'),
        ),
        migrations.AddField(
            model_name='good',
            name='height',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='good',
            name='hypoallergenic',
            field=models.BooleanField(default=False, verbose_name='Гипоаллергенный'),
        ),
        migrations.AddField(
            model_name='good',
            name='image_for_cart',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка для корзины'),
        ),
        migrations.AddField(
            model_name='good',
            name='mattress_type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Тип матраса'),
        ),
        migrations.AddField(
            model_name='good',
            name='maximum_load_on_one_berth',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Макс. нагрузка на одно спальное место'),
        ),
        migrations.AddField(
            model_name='good',
            name='size',
            field=models.CharField(blank=True, max_length=50, verbose_name='Размер'),
        ),
        migrations.AddField(
            model_name='good',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='slides',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.goodscategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='good',
            name='characters',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='good',
            name='feedbacks',
            field=djrichtextfield.models.RichTextField(blank=True, verbose_name='Отзывы'),
        ),
        migrations.AlterField(
            model_name='good',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='good',
            name='popularity',
            field=models.IntegerField(blank=True, default=1, verbose_name='Популярность'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='good',
            name='quolity',
            field=models.IntegerField(blank=True, default=1, verbose_name='Качество'),
        ),
        migrations.AlterField(
            model_name='good',
            name='rigidity',
            field=models.CharField(max_length=50, verbose_name='Жесткость'),
        ),
        migrations.AlterField(
            model_name='good',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='good',
            name='weight',
            field=models.BigIntegerField(verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='goods_height',
            name='height',
            field=models.BigIntegerField(blank=True, default=20, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='goods_icons',
            name='icons',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Иконки'),
        ),
        migrations.AlterField(
            model_name='goods_images',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='goods_sizes',
            name='size',
            field=models.CharField(blank=True, max_length=50, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='cat',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя заказчика')),
                ('telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Заказчика')),
                ('agreement', models.BooleanField(default=False, verbose_name='Соглашение с правилами')),
                ('status', models.CharField(choices=[('Новый заказ', 'Новый заказ'), ('В процессе', 'Заказ в обработке'), ('Готов', 'Заказ готов'), ('Завершен', 'Заказ выполнен')], default='Новый заказ', max_length=100, verbose_name='Статус заказ')),
                ('buying_type', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=100, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cart', to='main.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='main.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Goods_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True, verbose_name='ID объекта')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='Количество товара')),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10, verbose_name='Итоговая цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10, verbose_name='Старая цена')),
                ('sale', models.DecimalField(blank=True, decimal_places=2, default=20, max_digits=10, verbose_name='Скидка')),
                ('height', models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота')),
                ('size', models.CharField(blank=True, default='Не заполнено', max_length=50, verbose_name='Размер')),
                ('publish_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='main.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип содержимого')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Корзина товара',
                'verbose_name_plural': 'Корзина товара',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_order', to='main.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='main.Goods_Cart', verbose_name='Товары'),
        ),
        migrations.CreateModel(
            name='Goods_Cart_Proxy',
            fields=[
            ],
            options={
                'verbose_name': 'Сводная таблица товара',
                'verbose_name_plural': 'Сводная таблица товара',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.goods_cart',),
        ),
    ]
