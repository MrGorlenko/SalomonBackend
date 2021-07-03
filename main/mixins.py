from django.views.generic import View
from .models import *


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            last_cart_id = Cart.objects.latest('id')
            if request.user.is_authenticated:
                customer = Customer.objects.filter(session_id=ip).first()
                if not customer:
                    customer = Customer.objects.create(
                        session_id=ip
                    )
                cart = Cart.objects.filter(owner=customer).first()
                if not cart:
                    cart = Cart.objects.create(
                        id=str(last_cart_id.id + 1),
                        owner=customer
                    )
            else:
                customer = Customer.objects.filter(session_id=ip).first()
                if not customer:
                    customer = Customer.objects.create(
                        session_id=ip
                    )
                cart = Cart.objects.filter(owner=customer).first()
                if not cart:
                    cart = Cart.objects.create(
                        id=str(last_cart_id.id + 1),
                        owner=customer
                    )
            self.cart = cart
            return super().dispatch(request, *args, **kwargs)
        except:
            last_cart_id = 0
            if request.user.is_authenticated:
                customer = Customer.objects.filter(session_id=ip).first()
                if not customer:
                    customer = Customer.objects.create(
                        session_id=ip
                    )
                cart = Cart.objects.filter(owner=customer).first()
                if not cart:
                    cart = Cart.objects.create(
                        id=last_cart_id + 1,
                        owner=customer
                    )
            else:
                customer = Customer.objects.filter(session_id=ip).first()
                if not customer:
                    customer = Customer.objects.create(
                        session_id=ip
                    )
                cart = Cart.objects.filter(owner=customer).first()
                if not cart:
                    cart = Cart.objects.create(
                        id=last_cart_id + 1,
                        owner=customer
                    )
            self.cart = cart
            return super().dispatch(request, *args, **kwargs)
