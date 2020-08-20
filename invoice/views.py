from django.shortcuts import render, redirect
from pos.models import Product, Customer, Order, OrderItem
from pos.forms import ProductForm
import csv
from django.http import HttpResponse
import json
import itertools

def invoice_dashboard(request):
    return render(request, 'invoice_dashboard.html')

def sold_products(request):
    product = Product.objects.all()
    form = ProductForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        lst = [(names[0]) for names in Product.objects.values_list('name')]
        
        form.save() if name not in lst else print(lst)
    
    
    
    context={'product':product,'form':form}
    return render(request, 'sold_products.html', context)

def customer_invoice(request):
    if request.method == 'POST':
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(identity=cid)
        
        customer_orders = Order.objects.filter(customer=cid).filter(success=True)
        one=[]
        two=[]
        three=[]
        four=[]
        summ=[]
        
        for i in range(0,len(customer_orders)):
            one.append(customer_orders[i])
        
        for i in range(0,len(one)):
            two.append(OrderItem.objects.filter(order_id=one[i]))
        #print(two)
        for each in range(0,len(two)):
            
            for indi in range(0,len(two[each])):
                three.append(two[each][indi].product)
                four.append(two[each][indi].id)
                summ.append(two[each][indi].product.price)
                
        
        customer_invoice.total = sum([int(summitem) for summitem in summ])
        print(customer_invoice.total)
        context = {'orders': [order for order in customer_orders],
                'total': sum([int(summitem) for summitem in summ]),
                'customer': customer,
                'three':three,
                'four':four,
                'summ':summ}
        
        return render(request, 'customer_invoice_detail.html', context)
    else:
        return render(request, 'customer_invoice.html')




def split(request):
    print(customer_invoice.total)
    total = customer_invoice.total
    context = {'total': total}
    return render(request, 'split.html', context)

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



def delete_that_list(request, orderitem_id=None):
    orderitem=OrderItem.objects.get(id=orderitem_id)
    print(orderitem)
    
    orderitem.delete()
    return redirect("customer_invoice")
    
    
    
    
def export_users_xls(request):
    response = HttpResponse(content_type='text/csv')
    
    writer=csv.writer(response)
    writer.writerow(['Product Name', 'Remaining' , 'Product Price', 'Sold', 'Total price' , ])
    # Sheet header, first row
    for member in Product.objects.all().values_list('name', 'present_item', 'price','ordered_times'):
        tot = int(member[2]) * member[3]
        member = member + (tot,)
               
        writer.writerow(member)

    response['Contet-Disposition'] = 'attachment; filename = "products.csv"'
    
    return response

    
    
def clear(request):
    Product.objects.all().delete()
    return redirect("dashboard")
    
    