from django.contrib import admin
from .models import Item, Category, Order, OrderItem

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_name', 'category_price')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print('obj variable')
        obj.item_price = Item.objects.get(pk = obj.item.id).category.price
        obj.item_description = Item.objects.get(pk = obj.item.id).description
        super().save_model(request, obj, form, change)

admin.site.register(Order)