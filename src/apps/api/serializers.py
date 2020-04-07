from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.serializers import raise_errors_on_nested_writes

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'api_key')
        extra_kwargs = {
            'api_key': {'read_only': True},
        }
