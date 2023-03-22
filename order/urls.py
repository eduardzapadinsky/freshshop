"""
Order app URL Configuration

"""

from django.urls import path

from . import views

app_name = "order"
urlpatterns = [
    path("orders/create/<str:slug>/", views.OrderProduct.as_view(), name="order-create"),
    path("orders/", views.OrderListView.as_view(), name="order-list"),
    path("orders/refund/", views.RefundListView.as_view(), name="refund-list"),
    path("orders/refund/<int:id>/", views.CreateRefundOrder.as_view(), name="refund-create"),
    path("orders/refund/approve/<int:id>/", views.ApproveRefundOrder.as_view(), name="refund-approve"),
    path("orders/refund/disapprove/<int:id>/", views.DisapproveRefundOrder.as_view(), name="refund-disapprove"),
]
