from django import forms
from .models import ContactUs, Order

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'text', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام خود را وارد کنید...',
                'rows': 5
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('placeholder'):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': self.fields[field].label
                })


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'email', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@gmail.com'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'تعداد'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not self.fields[field].widget.attrs.get('placeholder'):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': self.fields[field].label
                })
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if len(phone) != 11:
            raise forms.ValidationError('شماره تماس باید ۱۱ رقم باشد')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تماس باید فقط شامل اعداد باشد')
        return phone