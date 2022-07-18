from django.contrib import admin
from .models import Product, Offers, Customers, Slot, Booking, Service, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pId', 'name', 'price', 'brandName', 'currentStock')

admin.site.register(Product, admin.ModelAdmin)

class OffersAdmin(admin.ModelAdmin):
    list_display = ('oId', 'name', 'code', 'percentOff')

admin.site.register(Offers, admin.ModelAdmin)


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('cId', 'name', 'email', 'phone', 'token')

admin.site.register(Customers, admin.ModelAdmin)

class SlotAdmin(admin.ModelAdmin):
    list_display = ('sId', 'slotDate', 'slotTime', 'slotAvailable')

admin.site.register(Slot, admin.ModelAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('bId', 'customer', 'slot', 'service' ,'dateCreated')

admin.site.register(Booking, admin.ModelAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('sId', 'name', 'price')

admin.site.register(Service, admin.ModelAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('oId', 'name', 'email', 'orderTotal')

admin.site.register(Order, admin.ModelAdmin)

