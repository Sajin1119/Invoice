from rest_framework import serializers
from .models import Invoice, InvoiceDetail


#seriliazing Invoice Detail 
class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'


#seriliazing Invoice Detail 
class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
