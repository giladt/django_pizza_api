from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=64)

    def __str__(self):
        return self.client_name


class Flavour(models.Model):
    flavour_name = models.CharField(max_length=64)

    def __str__(self):
        return self.flavour_name


class Size(models.Model):
    size_name = models.CharField(max_length=64)

    def __str__(self):
        return self.size_name


class OrderStatus(models.Model):
    order_status_name = models.CharField(max_length=32)

    def __str__(self):
        return self.order_status_name


class Item(models.Model):
    flavour = models.ForeignKey(Flavour, models.CASCADE, related_name="flavour", default=None)
    size = models.ForeignKey(Size, models.CASCADE, related_name="size", default=None)
    amount = models.IntegerField(
        name="amount",
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        default=1,
    )
    isReady = models.BooleanField(name="is_ready", default=False)

    class Meta:
        unique_together = ("flavour", "size")

    def __str__(self) -> str:
        return (
            self.flavour.flavour_name
            + " "
            + str(self.size.size_name)
            + " x"
            + str(self.amount)
        )


class Order(models.Model):
    order_time = models.DateTimeField(auto_now_add=True)
    order_update_time = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, models.CASCADE, related_name="client", default=None)
    order_status = models.ForeignKey(OrderStatus, models.CASCADE, related_name="order_status", default=None)

    def __str__(self):
        return str(self.client) + " (" + str(self.order_time) + ")"


class OrderItems(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, related_name="order", default=None)
    item = models.OneToOneField(Item, models.CASCADE, related_name="item", primary_key=True, default=None)

    class Meta:
        unique_together = ("order", "item")
