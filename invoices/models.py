from django.db import models
from .custom_fields import SaleItemsListField


class Party(models.Model):
    name = models.CharField(max_length=100)
    GST_no = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()


class Invoice(models.Model):
    invoice_no = models.IntegerField(primary_key=True)
    invoice_to = models.ForeignKey(Party, null=True, on_delete=models.SET_NULL)
    date_of_invoice = models.DateField()
    dispatch = models.CharField(max_length=100)
    mode_of_payment = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    state_and_code = models.CharField(max_length=100)
    waybill_no = models.CharField(blank=True, max_length=100)
    sale_items = SaleItemsListField()
    created = models.DateTimeField(auto_now_add=True)
