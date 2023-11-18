from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header='E-commerce Site'
admin.site.site_title = 'Shop'
admin.site.index_title='Manage Shoppin'

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category = 'default')

    change_category_to_default.short_description = 'Default'
    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title')
    actions=('change_category_to_default',)
    fields=('title', 'price',)
    list_editable = ('price',)

admin.site.register(Products)
admin.site.register(Order)