from django.shortcuts import render, redirect
from pos.models import Product, Customer, Order, OrderItem
import json

def invoice_dashboard(request):
    return render(request, 'invoice_dashboard.html')

def customer_invoice(request):
    if request.method == 'POST':
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(identity=cid)
        print(customer)
        customer_orders = Order.objects.filter(customer=cid).filter(success=True)

        
        oitem=OrderItem.objects.filter(order_id=customer_orders[0])
        context = {'orders': [order for order in customer_orders],
                'total': sum([int(order.total_price) for order in customer_orders]),
                'customer': customer,
                'oitem':oitem}
        
        print([order for order in oitem])
        return render(request, 'customer_invoice_detail.html', context)
    else:
        return render(request, 'customer_invoice.html')

def remove(request):
    if request.method == 'POST':
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(identity=cid).delete()
        print(customer)
        return redirect("customer_invoice")
    else:
        return render(request, 'customer_delete.html')
        
        
        
def deleteitem(request, order_id=None):
    order=Order.objects.get(id=order_id)
    order.delete()
    return redirect("customer_invoice")
