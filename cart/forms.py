from django import forms
from .models import Product


class ProductForm(forms.Form):
    title = forms.ChoiceField((
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ),
        required=False,
        label='Select product'
    )
