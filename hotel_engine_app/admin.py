from django.contrib import admin

# Register your models here.
from .models import Customer, Hotel, Manager, Receptionist, Order, Review

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Receptionist)
admin.site.register(Hotel)
admin.site.register(Order)
admin.site.register(Review)
