# Create your tests here.
from django.test import TestCase
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceAPITestCase(TestCase):
    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        self.assertEqual(response.data, serializer.data)
