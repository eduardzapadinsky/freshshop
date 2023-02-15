"""
Order app URL Configuration

"""

from django.urls import path

from . import views

app_name = "order"
urlpatterns = [
    path("orders/create/<str:slug>/", views.OrderProduct.as_view(), name="order-create"),
    path("orders/", views.OrderListView.as_view(), name="order-list"),
]
