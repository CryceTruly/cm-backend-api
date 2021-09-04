from rest_framework import serializers
from .models import Campaign,Subscriber



class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model=Campaign
        fields="__all__"



class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model=Subscriber
        fields="__all__"