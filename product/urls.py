"""
Product app URL Configuration

"""

from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path("", views.ProductsListView.as_view(), name="homepage"),
    path("products/", views.ProductsListView.as_view(), name="product-list"),
    path("products/create/", views.ProductsCreateView.as_view(), name="product-create"),
    path("products/<str:slug>/", views.ProductsDetailView.as_view(), name="product-detail"),
    path("products/<str:slug>/update/", views.ProductsUpdateView.as_view(), name="product-update"),
]
