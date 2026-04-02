from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(products)
class products_deatils(admin.ModelAdmin):
    list_display=['name','price','quantity','description','image','bill','register_at']
    list_filter=['name','description']
    search_fields=['name']
    ordering=['name']
    list_per_page=20