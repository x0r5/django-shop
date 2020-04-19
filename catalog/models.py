from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(null=False, blank=False, db_index=True, unique=True, max_length=20, verbose_name="The Category's name")
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")
    label = models.CharField(null=True, blank=True, db_index=True, verbose_name="Display Name", max_length=100)

    def __str__(self):
        return self.name

    def get_products(self):
        return Product.objects.filter(category=self)
    
class Product(models.Model):
    name = models.CharField(null=False, blank=False, db_index=True, unique=True, max_length=20, verbose_name="The Product's name")
    label = models.CharField(null=True, blank=True, db_index=True, max_length=100, verbose_name="Display Name")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    price = models.IntegerField()
    description = models.CharField(null=True, blank=True, max_length=300, verbose_name="Product description")
    available = models.BooleanField(help_text="True if available",default=True)
    orderable = models.BooleanField(help_text="True if placing orders is allowed", default=True)
    tax_mode = models.IntegerField(default=17, help_text="Tax value on product. Default is 17%")


    def gross_price(self):
        return self.price * self.tax_mode