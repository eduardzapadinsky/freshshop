from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "description", "price", "count", "picture"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not self.initial:
            try:
                Product.objects.get(name=name)
                raise ValidationError("Name exists. Choose another one.")
            except IntegrityError:
                return name
        else:
            return name
