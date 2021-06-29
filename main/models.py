from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from djrichtextfield.models import RichTextField
from django.urls import reverse


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


class GoodsCategory(models.Model):
    cat = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return f'{self.cat}'

    def get_absolute_url(self):
        return get_product_url(self, 'item')


class Good(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=50, default='Matress')
    rigidity = models.CharField(max_length=50, default='Soft')
    weight = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=20)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=20)
    popularity = models.IntegerField(blank=True, default=1)
    quolity = models.IntegerField(blank=True, default=1)
    description = RichTextField(blank=True, default='')
    characters = RichTextField(blank=True, default='')
    feedbacks = RichTextField(blank=True, default='')
    image_for_cart = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return get_product_url(self, 'item')


class Goods_Images(models.Model):
    prop = models.ForeignKey(Good, related_name='Image', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.prop.title


class Goods_Sizes(models.Model):
    prop = models.ForeignKey(Good, related_name='Size', on_delete=models.CASCADE)
    size = models.CharField(max_length=50, blank=True)


class Goods_Icons(models.Model):
    prop = models.ForeignKey(Good, related_name='Icons', on_delete=models.CASCADE)
    icons = models.ImageField(blank=True)


class Goods_Height(models.Model):
    prop = models.ForeignKey(Good, related_name='Height', on_delete=models.CASCADE)
    height = models.BigIntegerField(blank=True, default=20)


class Goods_Cart(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=20)

    def __str__(self):
        return 'Продукт: {}'.format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Customer(models.Model):
    session_id = models.CharField(max_length=40, null=True)

    def __str__(self):
        return str(self.session_id)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(Goods_Cart, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    in_order = models.BooleanField(default=False)
    for_anonymous_users = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
