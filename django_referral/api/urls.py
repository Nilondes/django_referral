from django.urls import path
from .views import ReferralListView


urlpatterns = [
    path("referals/<int:pk>", ReferralListView.as_view())
]