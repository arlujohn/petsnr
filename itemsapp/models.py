from django.db import models

# Create your models here.
class Item(models.Model):
    # We need item id, item name, item description, item price, item stock
    item_id = models.AutoField(primary_key=True,auto_created=True)
    item_name = models.CharField(max_length=64)
    item_description = models.CharField(max_length=120)
    item_category = models.CharField(max_length=120,default="Misc")
    item_price = models.IntegerField()
    item_stock = models.IntegerField()

    # This is a string representation of the tours
    def __str__(self):
        return(f"ID:{self.item_id}: Item Name: {self.item_name} Item Description: {self.item_description} Item Category: {self.item_category} Item Price: {self.item_price} Item Stock: {self.item_stock}")

    