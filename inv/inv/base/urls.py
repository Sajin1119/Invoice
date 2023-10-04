from django.urls import path
from . import views

urlpatterns = [
    path('invoices/',views.invoice),
    path('invoices/<int:id>/', views.invoice_detail),
    ]
