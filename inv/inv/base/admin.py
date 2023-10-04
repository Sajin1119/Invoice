from django.contrib import admin
from .models import Invoice,InvoiceDetail

# Register your models here.


#registering models form models.py to admin dashboard
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)