from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form for product
    """

    class Meta:
        model = Product
        fields = ["name", "description", "price", "count", "picture"]

    def clean_name(self):
        """
        Check name only for create method
        """
        name = self.cleaned_data["name"]
        if not self.initial:
            try:
                Product.objects.get(name=name)
                raise ValidationError("Name exists. Choose another one.")
            except Product.DoesNotExist:
                return name
        else:
            return name
