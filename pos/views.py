from django.shortcuts import render, redirect
import json
from django.http import HttpResponseRedirect
from .forms import CustomerForm
from .models import Product, Customer, Order, OrderItem


def dashboard(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context={'form':form}
    return render(request, 'dashboard.html',context)
    

  
      

def billing(request):
    if request.method == 'GET':
        
        return render(request, 'billing.html')
    else:
        
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(pk=cid)
        products = list(Product.objects.all())
        # context = { 'cust' : customer.identity,
        #             'name' : customer.name,
        #             'balance' : customer.balance,
        #             'products': products, }
        return render(request, 'billing_details.html', {'customer': customer, 'products': products})








def order(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        print(data)
        if data is None:
            raise AttributeError
        print(data)
        customer = Customer.objects.get(pk=data['customer_id'])
        order = Order.objects.create(customer=customer,
                                    total_price=data['total_price'],
                                    success=False)
                                    
        for product_id in data['product_ids']:
            product=Product.objects.get(pk=product_id)
            OrderItem( product=product, order=order).save()
            if product.present_item > 0:
                product.present_item = product.present_item - 1
                product.ordered_times=product.ordered_times + 1
                product.save()
                if data['total_price'] <= customer.balance:
                    customer.balance -= int(data['total_price'])
                    customer.save()
                    order.success = True
            
        
        order.save()
        return render(request, 'order.html', {'success' : order.success})
    
