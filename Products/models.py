from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=128, verbose_name="category name")

    class Meta:
        db_table = "Categories"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=128,verbose_name="product name")
    description = models.CharField(max_length=256, verbose_name="description")
    stock = models.IntegerField(verbose_name="stock", default = 0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits= 10, decimal_places=3, default=0,validators=[MinValueValidator(0)])
    discount = models.PositiveIntegerField(default=0, verbose_name="discount-percentage",validators=[MaxValueValidator(100)])

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.name


