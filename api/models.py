from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=64)

    def __str__(self):
        return self.client_name


# Create your models here.
