from django import forms

from .models import Order, Refund


class OrderForm(forms.Form):
    count = forms.DecimalField(required=True, label="Count",
                               widget=forms.NumberInput(attrs={
                                   "class": "form-control",
                                   "value": 0,
                                   "min": 0
                               }))

    class Meta:
        model = Order
        fields = ["count"]
