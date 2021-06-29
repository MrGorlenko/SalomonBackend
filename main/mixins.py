from django.views.generic import View
from .models import *


class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(session_id=request.session.session_key).first()
            if not customer:
                customer = Customer.objects.create(
                    session_id=request.session.session_key
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)
