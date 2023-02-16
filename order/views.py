from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
import datetime
from django.db import IntegrityError

from product.models import Product
from .models import Order, Refund
from .forms import OrderForm
from user.models import UserModel


def delta_date():
    date_expire = datetime.datetime.now() - datetime.timedelta(hours=40)
    return date_expire


class OrderProduct(View):
    """
    Order product by user
    """

    def post(self, request, slug):
        form = OrderForm(request.POST)
        user = UserModel.objects.get(id=request.user.id)
        product = Product.objects.get(slug=slug)

        if form.is_valid():
            cd = form.cleaned_data
            count = cd["count"]
            order_sum = product.price * count
            message_count = count <= product.count
            message_delta = order_sum <= user.wallet
            if message_count and message_delta:
                Order.objects.create(user=user, count=count, product=product)
                user.wallet -= order_sum
                user.save()
                product.count -= count
                product.save()
                return redirect("order:order-list")
            if not message_count:
                messages.warning(request, "Not enough goods available!")
            if not message_delta:
                messages.warning(request, "You haven't enough money in your site wallet!")
            return redirect("product:product-detail", slug)


class RefundOrder(View):
    """
    Refund order by user
    """

    def get(self, request, id):
        order = Order.objects.get(id=id)
        if order.created.timestamp() > delta_date().timestamp():
            try:
                Refund.objects.create(order=order)
            except IntegrityError:
                messages.warning(request, "The refund has already been created. Look at 'REFUNDS'")
                return redirect("order:order-list")
        else:
            messages.warning(request, "Time is over. You couldn't bring it back anymore!")
            return redirect("order:order-list")
        return redirect("order:refund-list")


class OrderListView(ListView):
    """
    List of user orders
    """
    model = Order

    def get_queryset(self):
        user = UserModel.objects.get(id=self.request.user.id)
        queryset = Order.objects.filter(user=user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["date_expire"] = delta_date()
        return context


class RefundListView(ListView):
    """
    List of user refunds
    """
    model = Refund

    def get_queryset(self):
        user = UserModel.objects.get(id=self.request.user.id)
        queryset = Refund.objects.filter(order__user=user)
        return queryset
