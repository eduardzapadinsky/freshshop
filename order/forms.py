from django import forms

from .models import Order


class OrderForm(forms.Form):
    count = forms.DecimalField(required=True, label="Count",
                               widget=forms.NumberInput(attrs={
                                   "class": "form-control",
                                   "value": 1,
                                   "min": 0.1
                               }))

    class Meta:
        model = Order
        fields = ["count"]


