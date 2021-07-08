from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from djrichtextfield.models import RichTextField
from django.urls import reverse
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={
        'ct_model': ct_model,
        'slug': obj.slug,
    })


class Slides(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    typeof = models.CharField(max_length=8)
    price = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Слайдеры'
        verbose_name_plural = 'Слайдеры'


class GoodsCategory(models.Model):
    cat = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(unique=True, null=True, verbose_name='Ссылка')

    def __str__(self):
        return f'{self.cat}'

    def get_absolute_url(self):
        return get_product_url(self, 'item')

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'


class Good(models.Model):
    category = models.ForeignKey(GoodsCategory,
                                 related_name='category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория'
                                 )
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(unique=True, null=True, verbose_name='Ссылка')
    title = models.CharField(max_length=50, verbose_name='Название товара')
    rigidity = models.CharField(max_length=50, verbose_name='Жесткость')
    weight = models.BigIntegerField(verbose_name='Масса')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=20,
                                verbose_name='Цена'
                                )
    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    default=20,
                                    verbose_name='Старая цена')
    popularity = models.IntegerField(blank=True, default=1, verbose_name='Популярность')
    quolity = models.IntegerField(blank=True, default=1, verbose_name='Качество')
    description = RichTextField(blank=True, verbose_name='Описание')
    characters = RichTextField(blank=True, verbose_name='Характеристики')
    feedbacks = RichTextField(blank=True, verbose_name='Отзывы')
    image_for_cart = models.ImageField(blank=True, verbose_name='Картинка для корзины')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return get_product_url(self, 'item')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Goods_Images(models.Model):
    prop = models.ForeignKey(Good, related_name='Image', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.prop.title

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинка товара'


class Goods_Sizes(models.Model):
    prop = models.ForeignKey(Good, related_name='Size', on_delete=models.CASCADE)
    size = models.CharField(max_length=50, blank=True, verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер товара'
        verbose_name_plural = 'Размер товара'


class Goods_Icons(models.Model):
    prop = models.ForeignKey(Good, related_name='Icons', on_delete=models.CASCADE)
    icons = models.ImageField(blank=True, verbose_name='Иконки')

    class Meta:
        verbose_name = 'Иконка товара'
        verbose_name_plural = 'Товара товара'


class Goods_Height(models.Model):
    prop = models.ForeignKey(Good, related_name='Height', on_delete=models.CASCADE)
    height = models.BigIntegerField(blank=True, default=20, verbose_name='Высота')

    class Meta:
        verbose_name = 'Высота товара'
        verbose_name_plural = 'Высота товара'


class Goods_Cart(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     verbose_name='Тип содержимого'
                                     )
    object_id = models.PositiveIntegerField(null=True, verbose_name='ID объекта')
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    final_price = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True, default=20,
                                      verbose_name='Итоговая цена')
    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    default=20,
                                    verbose_name='Старая цена'
                                    )
    sale = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               blank=True,
                               default=20,
                               verbose_name='Скидка'
                               )
    height = models.IntegerField(null=True, default=0, verbose_name='Высота', blank=True)
    size = models.CharField(max_length=50, blank=True, verbose_name='Размер')
    publish_date = models.DateField(verbose_name='Дата', default=timezone.now)

    def __str__(self):
        return 'Продукт: {}'.format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        self.old_price = self.qty * self.content_object.old_price
        self.sale = self.qty * self.content_object.old_price - self.qty * self.content_object.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина товара'
        verbose_name_plural = 'Корзина товара'


class Goods_Cart_Proxy(Goods_Cart):
    class Meta:
        proxy = True
        verbose_name = 'Сводная таблица товара'
        verbose_name_plural = 'Сводная таблица товара'


class Customer(models.Model):
    session_id = models.GenericIPAddressField(max_length=40,
                                              null=True,
                                              verbose_name='IP пользователя'
                                              )
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return str('Пользователь с IP-адресом {}'.format(self.session_id))

    class Meta:
        verbose_name = 'IP пользователя товара'
        verbose_name_plural = 'IP пользователя товара'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(Goods_Cart, blank=True,
                                      related_name='related_cart', verbose_name='Товары')
    total_products = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    final_price = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      blank=True, default=0,
                                      verbose_name='Итоговая цена')
    in_order = models.BooleanField(default=False, verbose_name='Занятая корзина')
    for_anonymous_users = models.BooleanField(default=False, verbose_name='Для анонимов')
    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    default=0,
                                    verbose_name='Старая цена')
    sale = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               blank=True,
                               default=0,
                               verbose_name='Скидка')

    def __str__(self):
        return str("Корзина №{}".format(self.id))

    def save(self, *args, **kwargs):
        cart_data = self.products.aggregate(models.Sum('final_price'), models.Count('id'))
        old_price = self.products.aggregate(models.Sum('old_price'), models.Count('id'))
        sale = self.products.aggregate(models.Sum('sale'), models.Count('id'))
        if cart_data.get('final_price__sum'):
            self.final_price = cart_data['final_price__sum']
            self.old_price = old_price['old_price__sum']
            self.sale = sale['sale__sum']
        else:
            self.final_price = 0
            self.old_price = 0
            self.sale = 0
        self.total_products = cart_data['id__count']
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Order(models.Model):
    STATUS_NEW = 'Новый заказ'
    STATUS_IN_PROGRESS = 'В процессе'
    STATUS_READY = 'Готов'
    STATUS_COMPLETED = 'Завершен'

    BUYING_TYPE_SELF = 'Самовывоз'
    BUYING_TYPE_DELIVERY = 'Доставка'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    name = models.CharField(null=True, max_length=100, verbose_name='Имя заказчика', blank=True)
    telephone = PhoneNumberField(null=True, blank=True, unique=False)
    email = models.EmailField(null=True, blank=True, verbose_name='Email Заказчика')
    agreement = models.BooleanField(default=False, verbose_name='Соглашение с правилами')
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders',
                                 on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='Cart')
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str("Заказ №{}".format(self.id))

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
