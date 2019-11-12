from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self):
        return self.name

    