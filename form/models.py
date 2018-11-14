from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_desc = models.TextField()
    product_price = models.DecimalField(decimal_places=2, max_digits=4)



