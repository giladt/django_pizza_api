from rest_framework.serializers import ModelSerializer
from .models import *


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "client_name", "client_address", "client_phone"]


class FlavourSerializer(ModelSerializer):
    class Meta:
        model = Flavour
        fields = ["id", "flavour_name"]


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size_name"]


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "status_name"]

