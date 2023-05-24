from rest_framework.serializers import ModelSerializer
from .models import *


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "client_name", "client_address", "client_phone"]

