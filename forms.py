from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

"""
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Or Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}))
"""



class LoginForm(forms.Form):

    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 11:
            raise ValidationError('تلفن وارد شده باید ۱۱ رقم باشد', 'invalid_phone')
        return phone

    def start_with_0(value):
        if value[0] != '0':
            raise forms.ValidationError('اول شماره باید با 0 شروع شود مثال : 09124564231')


