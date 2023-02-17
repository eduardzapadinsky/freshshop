from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from order.forms import OrderForm
from .models import Product
from .forms import ProductForm


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Superuser-only permission
    """

    def test_func(self):
        return self.request.user.is_superuser


class ProductBaseView(LoginRequiredMixin, View):
    """
    Base view for Product views
    """
    model = Product
    form_class = ProductForm


class ProductsListView(ProductBaseView, ListView):
    """
    List of goods
    """


class ProductsDetailView(ProductBaseView, DetailView):
    """
    Product page
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_order"] = OrderForm()
        return context


class ProductsCreateView(SuperuserRequiredMixin, ProductBaseView, CreateView):
    """
    Create product page
    """
    template_name = "product/product_form.html"

    def get_success_url(self):
        return reverse('product:product-detail', kwargs={'slug': self.object.slug})


class ProductsUpdateView(ProductsCreateView, UpdateView):
    """
    Update product page
    """
