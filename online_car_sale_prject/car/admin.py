from django.contrib import admin
from. models import Car,Comment,BuyedCar
from django.contrib.auth.models import User

# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("user",)}
    list_display=["user","slug"]
admin.site.register(BuyedCar,BuyerAdmin)
admin.site.register(Comment)
admin.site.register(Car)
