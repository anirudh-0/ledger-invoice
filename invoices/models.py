from django.db import models


class SaleItem(models.Model):
    item_name = models.CharField(max_length=100)
    

class Invoice(models.Model):
    invoice_to = models.CharField(max_length=150)
    sale_items = models.ManyToManyField('SaleItem')
