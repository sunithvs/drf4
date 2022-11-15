"""
this file is for defining the serializers for the models
"""
from rest_framework import serializers
from home.models import Session, Coupon


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'  # this is for all the fields


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'  # this is for all the fields
