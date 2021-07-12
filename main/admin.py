from django.contrib import admin
from django.db.models import Sum
from main.models import *
import csv
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path
from datetime import date
import sys

admin.site.site_header = "Административная панель магазина Salamon"
admin.site.site_title = "Портал Salamon"
admin.site.index_title = "Добро пожаловать в Salamon"


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        name = "Выгрузка(Дата выгрузки {}).csv".format(date.today())
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = "attachment; filename=" + escape_uri_path(name)
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow([
            'Имя заказчика',
            'Телефон',
            'Email Заказчика',
            'Соглашение с правилами',
            'Покупатель',
            'Корзина',
            'Статус заказа',
            'Тип заказа',
            'Комментарий к заказу',
            'Дата получения заказа',
        ])

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Выгрузить данные"


class PropsImages(admin.TabularInline):
    model = Goods_Images


class PropsSizes(admin.TabularInline):
    model = Goods_Sizes


class PropsIcons(admin.TabularInline):
    model = Goods_Icons


class PropsHeight(admin.TabularInline):
    model = Goods_Height
    extra = 1
    show_change_link = True


class PropsAdminImage(admin.ModelAdmin):
    inlines = [PropsImages, PropsSizes, PropsIcons, PropsHeight, ]


admin.site.register(Slides)
admin.site.register(GoodsCategory)
admin.site.register(Good, PropsAdminImage)


@admin.register(Goods_Cart)
class Goods_Cart_Admin(admin.ModelAdmin):
    list_display = ('get_content_object', 'cart',)
    list_per_page = sys.maxsize

    def get_content_object(self, obj):
        return obj.content_object.title

    get_content_object.short_description = 'Товары в корзине'


@admin.register(Customer)
class Customer_Admin(admin.ModelAdmin):
    list_display = ('session_id', 'get_orders',)
    list_filter = ('session_id',)
    list_per_page = sys.maxsize

    def get_orders(self, obj):
        return ", \n".join([p.name for p in obj.orders.all()])

    get_orders.short_description = 'Имя заказчика'


@admin.register(Cart)
class Cart_Admin(admin.ModelAdmin):
    list_display = ('get_id', 'get_products', 'total_products',)
    list_filter = ('products',)
    list_per_page = sys.maxsize

    def get_id(self, obj):
        return obj.id

    def get_products(self, obj):
        return ", \n".join([p.content_object.title for p in obj.products.all()])

    get_products.short_description = 'Товары в корзине'
    get_id.short_description = 'Корзина'


@admin.register(Order)
class Order_Admin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = 'admin/order_table.html'
    list_display = ('name', 'cart_count',)
    list_filter = ('name',)
    actions = ["export_as_csv"]
    list_per_page = sys.maxsize
    date_hierarchy = 'order_date'

    def cart_count(self, obj):
        return obj.cart.total_products

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        response.context_data['table'] = list(
            qs
                .values(
                'id',
                'name',
                'telephone',
                'email',
                'status',
                'buying_type',
                'comment',
                'order_date',
            )
        )

        return response

    cart_count.admin_order_field = 'cart'
    cart_count.short_description = 'Количесвто товара в заказе'


@admin.register(Goods_Cart_Proxy)
class Goods_Cart_Proxy_Admin(admin.ModelAdmin):
    change_list_template = 'admin/goods_cart_table.html'
    list_filter = ('publish_date',)
    date_hierarchy = 'publish_date'

    def get_content(self, obj):
        return obj.content_object.title

    get_content.short_description = 'Название товара'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        context = {
            'sum': Sum('final_price')
        }
        response.context_data['table'] = list(
            qs
                .annotate(**context)
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**context)
        )
        return response


@admin.register(Comments)
class Comments_Admin(admin.ModelAdmin):
    list_display = ('name', 'rating',)
    list_filter = ('rating',)
