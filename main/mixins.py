from django.views.generic import View
from .models import *


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if Cart.objects.exclude(products__isnull=True):
            last_cart_id = 0
        else:
            last_cart_id = Cart.objects.latest('id')
        if not request.user.is_authenticated:
            # customer = Customer.objects.filter(session_id=request.session.session_key).first()
            # if not customer:
            #    customer = Customer.objects.create(
            #        session_id=request.session.session_key
            #    )
            # cart = Cart.objects.filter(owner=customer, in_order=False).first()
            # if not cart:
            #    cart = Cart.objects.create(id=str(last_cart_id.id + 1), owner=customer, in_order=True)
            # else:
            cart = Cart.objects.filter().first()
            if not cart:
                cart = Cart.objects.create(id=str(last_cart_id.id + 1),
                                           owner=str(ip)
                                           )
                print(cart)
            self.cart = cart
        return super().dispatch(request, *args, **kwargs)
