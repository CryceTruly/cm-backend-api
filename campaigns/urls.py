from django.urls import path
from .views import CampaignListAPIView,CampaignDetailAPIView,SubscribeToCampaignAPIView

urlpatterns = [
    path('campaigns',CampaignListAPIView.as_view(), name="campaigns"),
    path('campaigns/<str:slug>',CampaignDetailAPIView.as_view(), name="campaign"),
    path('subscribers',SubscribeToCampaignAPIView.as_view(), name="subscribe")
    
]
