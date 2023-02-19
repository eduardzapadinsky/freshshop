from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.db import IntegrityError
import datetime

from product.models import Product
from user.models import UserModel
from .models import Order, Refund
from .forms import OrderForm
from product.views import SuperuserRequiredMixin


def delta_date():
    """
    Checking for time to refund goods
    """

    date_expire = datetime.datetime.now() - datetime.timedelta(minutes=3)
    return date_expire


class OrderProduct(LoginRequiredMixin, View):
    """
    Order product by user
    """

    def post(self, request, slug):
        """
        Create oder if valid
        """
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


class CreateRefundOrder(LoginRequiredMixin, View):
    """
    Create refund order by user
    """

    def get(self, request, id):
        """
        Create refund if valid
        """
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


class ApproveRefundOrder(SuperuserRequiredMixin, View):
    """
    Delete refund order by admin
    """

    def get(self, request, id):
        """
        Create refund if valid
        """
        try:
            refund_to_approve = Refund.objects.get(id=id)
            refund_order = refund_to_approve.order
            user = refund_to_approve.order.user
            product = refund_order.product
            user.wallet += product.price * refund_order.count
            user.save()
            refund_order.product.count += refund_order.count
            product.save()
            refund_to_approve.is_approved = True
            refund_to_approve.save()
            refund_order.is_deleted = True
            refund_order.save()
        except Refund.DoesNotExist:
            messages.warning(request, "There isn't refund order")
        return redirect("order:refund-list")


class DisapproveRefundOrder(SuperuserRequiredMixin, View):
    """
    Delete refund order by admin
    """

    def get(self, request, id):
        """
        Delete refund if valid
        """
        try:
            refund_to_disapprove = Refund.objects.get(id=id)
            refund_to_disapprove.delete()
        except Refund.DoesNotExist:
            messages.warning(request, "There isn't refund order")
        return redirect("order:refund-list")


class OrderListView(LoginRequiredMixin, ListView):
    """
    List of user orders. Admin can see all the orders
    """

    model = Order

    def get_queryset(self):
        """
        Create different queryset for user and admin
        """
        user = UserModel.objects.get(id=self.request.user.id)
        if user.is_superuser:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(user=user, is_deleted=False)
        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Add expire date to manage refunds
        """
        context = super().get_context_data(*args, **kwargs)
        context["date_expire"] = delta_date()
        return context


class RefundListView(LoginRequiredMixin, ListView):
    """
    List of user refunds
    """

    model = Refund

    def get_queryset(self):
        """
        Create different queryset for user and admin
        """
        user = UserModel.objects.get(id=self.request.user.id)
        if user.is_superuser:
            queryset = Refund.objects.all()
        else:
            queryset = Refund.objects.filter(order__user=user, is_approved=False)
        return queryset
