from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False, label='Изображение')
    title = forms.CharField(min_length=3, max_length=64, label='Модель принтера')
    description = forms.CharField(widget=forms.Textarea(), label='Описание')
    type_printer = forms.CharField(max_length=100, label='Тип принтера')
    cost = forms.IntegerField(min_value=0, label='Стоимость')
