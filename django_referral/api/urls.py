from django.urls import path
from .views import ReferralListView


urlpatterns = [
    path("referrals/<int:pk>", ReferralListView.as_view())
]
