from rest_framework import serializers
from users.models import Referral


class ReferralSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ["user", "phone"]