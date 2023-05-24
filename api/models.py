from django.db import models


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

