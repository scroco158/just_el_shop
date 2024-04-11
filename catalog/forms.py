from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if ('казино' in cleaned_data or
            'криптовалюта' in cleaned_data or
            'крипта' in cleaned_data or
            'биржа' in cleaned_data or
            'дешево' in cleaned_data or
            'бесплатно' in cleaned_data or
            'обман' in cleaned_data or
            'полиция' in cleaned_data or
            'радар' in cleaned_data):
            raise forms.ValidationError('Не корректное название продукта')
        return cleaned_data
