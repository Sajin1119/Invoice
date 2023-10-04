from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer



#get and post values
@api_view(['GET', 'POST'])
def invoice(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get and update values
@api_view(['GET', 'PUT'])
def invoice_detail(request, id):
    try:
        invoice_detail = InvoiceDetail.objects.get(pk=id)
    except InvoiceDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InvoiceDetailSerializer(invoice_detail)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InvoiceDetailSerializer(invoice_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
