from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from users.models import Referral
from .serializers import ReferralSerizlizer


class ReferralListView(views.APIView):
    def get(self, request, pk, format=None):
        referral = Referral.objects.filter(user_id=pk)
        serialized = ReferralSerizlizer(referral, many=True)
        return Response(serialized.data)
