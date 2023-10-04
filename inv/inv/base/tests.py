# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'CustomerName': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {
            'invoice': self.invoice,
            'description': 'Test Description',
            'quantity': 2,
            'unit_price': '10.00',
            'price': '20.00',
        }
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_invoice(self):
        data = {'CustomerName': 'New Customer'}
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_get_invoice_detail(self):
        response = self.client.get(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = InvoiceDetailSerializer(self.invoice_detail)
        self.assertEqual(response.data, serializer.data)

    def test_update_invoice_detail(self):
        updated_data = {
            'description': 'Updated Description',
            'quantity': 3,
            'unit_price': '15.00',
        }
        response = self.client.put(f'/invoices/{self.invoice_detail.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice_detail.description, updated_data['description'])
        self.assertEqual(self.invoice_detail.quantity, updated_data['quantity'])
        self.assertEqual(str(self.invoice_detail.unit_price), updated_data['unit_price'])

    def test_get_nonexistent_invoice_detail(self):
        response = self.client.get('/invoices/999/')  # Assuming 999 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
