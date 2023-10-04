from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


#Invoice model
class Invoice(models.Model):
    Date=models.DateField(auto_now_add=True)
    CustomerName=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.CustomerName

#Invoice detailed model
class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_price(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"Invoice Number is: {self.invoice.pk},  Price is {self.calculate_price()}"
