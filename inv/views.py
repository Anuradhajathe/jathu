from django.shortcuts import render,redirect
from .models import Customer,Product,Tags,Order
from .forms import OrderForm

# Create your views here.
def dashboard(request):
    order=Order.objects.all()
    customer=Customer.objects.all()
    total_order=order.count()
    deliver=order.filter(status='Delivered').count()
    pending=order.filter(status='Pending').count()
    context={
        'order':order,
        'customer':customer,
        'total_order':total_order,
        'delivered':deliver,
        'pending':pending,

    }
    return render(request,'inv/dashboard.html',context)

def product(request):
    item=Product.objects.all()
    context={
        'item':item
    }
    return render(request,'inv/product.html',context)

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    order=customer.order_set.all()
    order_count=order.count()
    context={
        'pk_test':pk_test,
        'customer':customer,
        'order':order,
        'order_count':order_count,
    }
    return render(request,'inv/customer.html',context)

def create_order(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'inv/order_create.html',context)

def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form,}
    return render(request,'inv/order_create.html',context)

def delete_order(request,pk):
    order=Order.objects.get(id=pk)

    if request.method=="POST":
        order.delete()
        return redirect('/')
    
    context={'order':order,}
    return render(request,'inv/delete.html',context)
