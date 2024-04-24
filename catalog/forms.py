from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['is_moderated', 'product_owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_moderated':
                field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        check_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                       'бесплатно', 'обман', 'полиция', 'радар']
        for word in check_words:
            if cleaned_data.__contains__(word):
                raise forms.ValidationError('Не корректное название продукта')
        return cleaned_data


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_moderated', 'description', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_moderated':
                field.widget.attrs.update({'class': 'form-control'})


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
