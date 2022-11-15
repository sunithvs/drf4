"""
home/admin.py
"""

from django.contrib import admin
from .models import Session, Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']


class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'description', 'price', ]


admin.site.register(Coupon, CouponAdmin)
admin.site.register(Session, SessionAdmin)
