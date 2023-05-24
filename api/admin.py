from django.contrib import admin

from .models import *

admin.site.register(Client)
admin.site.register(Flavour)
admin.site.register(Size)
admin.site.register(OrderStatus)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItems)
