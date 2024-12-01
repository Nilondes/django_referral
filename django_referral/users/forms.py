from django import forms
from .models import User
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.Form):
    phone = PhoneNumberField()


class AuthNumberForm(forms.Form):
    auth_number = forms.IntegerField(max_value=9999)


class ReferralCodeForm(forms.Form):
    referral_code = forms.CharField(max_length=6)
