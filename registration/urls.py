"""
register/urls.py
"""
from django.urls import path, include
from rest_framework import routers
from registration import views

router = routers.DefaultRouter()

router.register(r'registration', views.RegistrationViewSet)

urlpatterns = [
    path("", router.urls),
]
