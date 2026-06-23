from django.contrib import admin
from .models import Food,FoodType,ContactUs,Order


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name','weight','length','price','old_price']
    list_display_links = ['name','weight','length','price','old_price']
    filter_horizontal = ['food_types']

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','text']
    list_display_links = ['name','email','phone_number','text']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','amount']
    list_display_links = ['name','email','phone_number','amount']    