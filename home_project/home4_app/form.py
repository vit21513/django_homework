from django import forms
from home2_app.models import Product


class Product_form(forms.Form):
    name = forms.CharField(label='Наименование', max_length=50)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    price = forms.FloatField(label='Цена', min_value=0)
    quantu = forms.IntegerField(label="количество", min_value=0)
    image = forms.ImageField()


class Product_add_foto(forms.Form):
    product = forms.ModelChoiceField(label='продукты', queryset=Product.objects.all())
    image = forms.ImageField()
