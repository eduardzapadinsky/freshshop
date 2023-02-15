from django.views.generic import ListView, DetailView

from order.forms import OrderForm
from .models import Product


class ProductsListView(ListView):
    """
    List of goods
    """
    model = Product


class ProductsDetailView(DetailView):
    """
    Product page
    """
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_order"] = OrderForm()
        return context
