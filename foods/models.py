from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_subtitle = models.CharField(max_length=20)
    item_desc = models.CharField(max_length=900)
    item_image = models.CharField(max_length=500, default="https://anvilhotel.com/wp-content/uploads/2017/08/food-placeholder.png")

    def __str__(self):
        return self.item_name
    
    