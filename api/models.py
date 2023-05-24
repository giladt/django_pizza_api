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


class Status(models.Model):
    status_name = models.CharField(max_length=32)

    def __str__(self):
        return self.status_name


class Order(models.Model):
    client = models.ForeignKey(Client, models.CASCADE, related_name="client")
    order_time = models.DateTimeField(auto_now_add=True)
    order_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.client) + " (" + str(self.order_time) + ")"


class Item(models.Model):
    flavour = models.ForeignKey(Flavour, models.CASCADE, related_name="flavour")
    size = models.ForeignKey(Size, models.CASCADE, related_name="size")
    status = models.ForeignKey(Status, models.CASCADE, related_name="status", default=1)
    order = models.ForeignKey(Order, models.CASCADE, related_name="order")
    amount = models.IntegerField(
        name="amount",
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        default=1,
    )

    class Meta:
        unique_together = ("flavour", "size", "order")

    def __str__(self) -> str:
        return (
            str(self.order.client.client_name)
            + " "
            + self.flavour.flavour_name
            + " x"
            + str(self.amount)
        )
