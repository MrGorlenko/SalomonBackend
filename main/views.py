from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, View
from main.models import *
from main.mixins import *


class Main_Page(CartMixin, View):

    def get(self, request, *args, **kwargs):
        print("Текущая сессия: {}".format(request.session.session_key))
        slides = Slides.objects.all()
        goodCategories = GoodsCategory.objects.all()
        goods = Good.objects.all()
        goodsImages = Goods_Images.objects.all()
        goodsHeight = Goods_Height.objects.all()
        goodSizes = Goods_Sizes.objects.all()
        goodIcons = Goods_Icons.objects.all()
        context = {
            'slides_list': slides,
            'goods_list': goods,
            'goods_images': goodsImages,
            'goods_height': goodsHeight,
            'goods_sizes': goodSizes,
            'goods_icons': goodIcons,
            'goods_cats': goodCategories,
            'cart': self.cart,
        }
        return render(
            request,
            'main/index.html',
            context=context
        )


class Items_Details(CartMixin, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'матрасы': Good,
        'кровати': Good,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Items_Details, self).get_context_data(**kwargs)
        context['images'] = Goods_Images.objects.all()
        context['ct_model'] = self.model
        return context

    context_object_name = 'item'
    template_name = 'main/item.html'
    slug_url_kwarg = 'slug'


class Cart_View(CartMixin, View):

    def get(self, request, *args, **kwargs):
        print("Текущая сессия: {}".format(request.session.session_key))
        category = GoodsCategory.objects.all()
        images = Goods_Images.objects.all()
        context = {
            'cart': self.cart,
            'category': category,
            'image': images,
        }
        return render(
            request,
            'main/basket.html',
            context=context
        )


class Add_To_Cart(CartMixin, View):

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        ct_model, slug = kwargs.get('ct_model'), kwargs.get('slug')
        product = Good.objects.get(pk=slug)
        cart_product, created = Goods_Cart.objects.get_or_create(
            user=self.cart.owner,
            cart=self.cart,
            content_type_id=1,
            object_id=product.id
        )
        if created:
            self.cart.products.add(cart_product)
        if name == 'buy':
            return HttpResponseRedirect('/')
        elif name == 'buy_on_click':
            return HttpResponseRedirect('/cart/')
        else:
            print('suka')