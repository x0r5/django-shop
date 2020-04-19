from django.contrib import admin

# Register your models here.
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'label', 'parent_category')

@admin.register(Product)
class ProductAdmin( admin.ModelAdmin):
    list_display = ('name', 'label', 'price', 'category', 'available', 'orderable', 'tax_mode')
    list_filter = ('category', 'available', 'orderable')