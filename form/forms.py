from django import forms

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(label='Product Name', max_length=100)
    product_desc = forms.CharField(label='Product Description',max_length=500)
    product_price = forms.DecimalField(label='Product Price', decimal_places=2, max_digits=4)