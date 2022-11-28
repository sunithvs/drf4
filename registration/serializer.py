"""
this file is for defining the serializers for the models for registration app
"""

from rest_framework import serializers

from home.models import Coupon
from registration.models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        # fields of Registration
        fields = ["name", "phone", "college", "attachment", "transaction_id"]

    """function for validating the coupon code"""

    def validate_coupon(self, value):
        if not value:
            return value
        coupon = Coupon.objects.filter(code=value).first()

        if coupon and coupon.is_active:
            return value
        else:
            raise serializers.ValidationError('Invalid coupon code')

    """function for validating the session"""

    def validate_session(self, value):
        if value.is_active:
            return value
        else:
            raise serializers.ValidationError('Invalid session')
