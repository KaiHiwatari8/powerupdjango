from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50, default='Product Title')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id':self.id})