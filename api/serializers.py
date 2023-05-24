from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["client_name", "client_address", "client_phone"]


class FlavourSerializer(ModelSerializer):
    class Meta:
        model = Flavour
        fields = ["flavour_name"]


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ["size_name"]


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ["order_status_name"]


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "flavour",
            "size",
            "amount",
            "is_ready",
        ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "client",
            "order_time",
            "order_update_time",
        ]


class OrderItemsSerializer(ModelSerializer):
    class Meta:
        model = OrderItems
        depth=2
        fields = "__all__"
