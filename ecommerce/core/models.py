from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=False, default=0.0)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self):
        return self.name

    def category_name(self):
        return self.category.name
    
    def category_price(self):   
        return self.category.price
    
    category_name.short_description = 'category'
    category_price.short_description = 'price'
    
class OrderItem(models.Model):
    # item = models.ForeignObject(Item, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete = models.CASCADE )
    count = models.IntegerField(null=False, default = 0)
    item_price = models.FloatField(null=True, default = 0)
    item_description = models.CharField(max_length = 255, blank = True, null = True)
    
    def __str__(self):
        return self.item.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order_item = models.ForeignKey(OrderItem, on_delete = models.CASCADE, null = True)
    start_date = models.DateTimeField(auto_now=True)
    order_date = models.DateTimeField(null=True)
    order = models.BooleanField(default=False)
    
    def __str__(self):
        return self.start_date
    
    