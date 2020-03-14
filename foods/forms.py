from django import forms 
from .models import Item

class FoodForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_subtitle", "item_desc", "item_image"]