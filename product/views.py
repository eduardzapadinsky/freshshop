from django.views.generic import ListView, DetailView

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
