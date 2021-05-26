from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    name = forms.CharField(
        label="Name:",
        required=False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Name Here!",
            }
        )
    )

    description = forms.CharField(
        label="Description:", 
        required=False,
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Descritptio Here!",
                "class":"form-control",
                "id":"id-class",
                "rows": 5,
                "cols": 16
            }
        )

    )

    price = forms.DecimalField(
        label="Price:", 
        initial=10.00
    )
    
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description'
        ]
    
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if "CFE" not in name.upper():
            raise forms.ValidationError("Name invalid.")
        return name
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price is None:
            raise forms.ValidationError("Price cannot be null.")
        if price < 10:
            raise forms.ValidationError("The minimum price is 10.00..")
        return price


class RawProductForm(forms.Form):

    name = forms.CharField(
        label="Name:",
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Title Here!",
            }
        )
    )

    description = forms.CharField(
        label="Description:", 
        required=False,
        widget = forms.Textarea(
            attrs = {
                "placeholder": "Descritptio Here!",
                "class":"form-control",
                "id":"id-class",
                "rows": 5,
                "cols": 16
            }
        )

    )
    price = forms.DecimalField(label="Price:", initial=10.00)