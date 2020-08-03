from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_dashboard, name='invoice_dashboard'),
    path('customer/', views.customer_invoice, name='customer_invoice'),
    path('delete/', views.remove, name ='remove'),
    path('deleteitem/<int:order_id>/',views.deleteitem, name="deleteitem"),
    path('delete_that_list/<int:orderitem_id>/', views.delete_that_list, name ='delete_that_list')
]
