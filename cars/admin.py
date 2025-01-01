from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name']

admin.site.register(Brand, BrandAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)
