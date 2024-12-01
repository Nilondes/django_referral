from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    referral_code = models.CharField(max_length=6, null=False, blank=False, unique=True)
    auth_number = models.IntegerField()

    def __str__(self):
        return f'{self.referral_code}'


class Referral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.user}'
