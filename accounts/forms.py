from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل خود را وارد کنید'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['email'].widget.attrs['placeholder'] = 'example@gmail.com'
        self.fields['password1'].widget.attrs['placeholder'] = 'رمز عبور (حداقل ۸ کاراکتر)'
        self.fields['password2'].widget.attrs['placeholder'] = 'تکرار رمز عبور'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['password'].widget.attrs['placeholder'] = 'رمز عبور'