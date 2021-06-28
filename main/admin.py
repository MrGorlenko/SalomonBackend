from django.contrib import admin
from main.models import *


# Register your models here.

class PropsImages(admin.TabularInline):
    model = Goods_Images


class PropsSizes(admin.TabularInline):
    model = Goods_Sizes


class PropsIcons(admin.TabularInline):
    model = Goods_Icons


class PropsHeight(admin.TabularInline):
    model = Goods_Height


class PropsAdminImage(admin.ModelAdmin):
    inlines = [PropsImages, PropsSizes, PropsIcons, PropsHeight, ]


admin.site.register(Slides)
admin.site.register(GoodsCategory)
admin.site.register(Good, PropsAdminImage)
admin.site.register(Goods_Cart)
admin.site.register(Customer)
admin.site.register(Cart)
