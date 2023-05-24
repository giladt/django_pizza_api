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


class OrderSerializer(ModelSerializer):
    status = StatusSerializer(many=False)
    client = ClientSerializer(many=False)

    class Meta:
        model = Order
        fields = [
            "client",
            "order_time",
            "order_update_time",
        ]


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "flavour",
            "size",
            "status",
            "order",
            "amount",
        ]
