from django import forms




class CreateOrderForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=False)

    requires_delivery = forms.TypedChoiceField(
        choices=[(True, 'Да'), (False, 'Нет')],
        coerce=lambda x: x == 'True',
        widget=forms.RadioSelect
    )
    
    payment_method = forms.TypedChoiceField(
        choices=[(False, 'Оплата картой'), (True, 'Наличными при получении')],
        coerce=lambda x: x == 'True',
        widget=forms.RadioSelect
    )