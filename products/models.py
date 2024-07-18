from django.db import models

# Create your models here.


class Brands (models.Model):

    brand_name = models.CharField(max_length=50)


class Category (models.Model):

    category = models.CharField(max_length=50)


class Genre (models.Model):

    SEX = {
        "M" : "Men",
        "F" : "Female",
        "U" : "Unisex",
        "N" : "Null",
    }

    sex = models.CharField(max_length=1, choices=SEX)


class ProductType (models.Model):

    type_name = models.CharField(max_length=50)
    

class Products (models.Model):

    name = models.CharField(max_length=50)
    inventory = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    sex = models.ForeignKey(Genre, blank=True, on_delete=models.CASCADE)

    variants = models.JSONField()
    
    # sku = models.CharField(max_length=20)
    # cost = models.FloatField()
    # upc = models.IntegerField()
    # weight = models.FloatField()
    # image_url = models.URLField()
    # msrp = models.FloatField()
    # additional_upc = models.IntegerField(blank=True)
    
    
    
    product_type = models.ForeignKey(ProductType, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name




