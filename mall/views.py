from django.shortcuts import render,get_object_or_404,redirect
from .models import Stuff,Cart,Order
from .forms import StuffForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime,timedelta
# Create your views here.

def index(request):
    stuffs=Stuff.objects.all()
    context={'stuffs':stuffs}
    return render(request,'mall/index.html',context)

def detail(request,stuff_id):
    stuff=Stuff.objects.get(id=stuff_id)
    context={'stuff':stuff}
    return render(request,'mall/detail.html',context)

def register(request):
    if request.method=="POST":
        stuff=Stuff(name=request.POST.get('name'),price=request.POST.get('price'),detail=request.POST.get('detail'),image=request.FILES.get('image'))
        stuff.pub_date=timezone.now()+timedelta(hours=9)
        stuff.save()
        return redirect('mall:index')
    else:
        form=StuffForm()
        return render(request,'mall/register.html',{'form':form})

@login_required(login_url='common:login')
def info(request):
    orderlists=Order.objects.filter(user=request.user)
    pub_times=[]
    orders=[]
    for orderlist in orderlists:
        pub_times.append(orderlist.order_date)
    pub_times=list(set(pub_times))
    for pub_time in pub_times:
        orderlists=Order.objects.filter(order_date=pub_time)
        orders.append(orderlists)
    context={'orderlists':orders,'username':request.user.username,'email':request.user.email}
    return render(request,'mall/info.html',context)

@login_required(login_url='common:login')
def cart(request):
    uCart=Cart.objects.filter(user=request.user)
    stuffs=uCart
    context={'stuffs':stuffs}
    return render(request,'mall/cart.html',context)

@login_required(login_url='common:login')
def addCart(request,stuff_id):
    uCart=Cart.objects.filter(user=request.user)
    stuff=Stuff.objects.get(id=stuff_id)
    for uCart2 in uCart:
        if uCart2.stuffs.id==stuff_id:
            uCart2.quantity+=1
            uCart2.save()
            break
    else:
        uCart2=Cart.objects.create(user=request.user,stuffs=stuff)
        uCart2.quantity+=1
        uCart2.save()
        
    return  redirect('mall:cart')

@login_required(login_url='common:login')
def subCart(request,stuff_id):
    uCart=Cart.objects.filter(user=request.user)
    for uCart2 in uCart:
        if uCart2.stuffs.id==stuff_id:
            uCart2.delete()
            break
    return  redirect('mall:cart')

@login_required(login_url='common:login')
def plusStuff(request,stuff_id):
    uCart=Cart.objects.filter(user=request.user)
    for uCart2 in uCart:
        if uCart2.stuffs.id==stuff_id:
            uCart2.quantity+=1
            uCart2.save()
            break
    return  redirect('mall:cart')

@login_required(login_url='common:login')
def minusStuff(request,stuff_id):
    uCart=Cart.objects.filter(user=request.user)
    for uCart2 in uCart:
        if uCart2.stuffs.id==stuff_id:
            uCart2.quantity-=1
            uCart2.save()
            if uCart2.quantity==0:
                uCart2.delete()
            break
    return  redirect('mall:cart')


@login_required(login_url='common:login')
def buyAtIndex(request,stuff_id):
    uCart=Cart.objects.filter(user=request.user)
    stuff=Stuff.objects.get(id=stuff_id)
    for uCart2 in uCart:
        if uCart2.stuffs.id==stuff_id:
            uCart2.quantity+=1
            uCart2.save()
            break
    else:
        uCart2=Cart.objects.create(user=request.user,stuffs=stuff)
        uCart2.quantity+=1
        uCart2.save()
    return  redirect('mall:cart')

@login_required(login_url='common:login')
def buy(request):
    subtotal=0
    order_date=datetime.now()
    if request.method == 'POST':
        uCarts=Cart.objects.filter(user=request.user)
        for uCart in uCarts:
            if request.POST.get(uCart.stuffs.name):
                stuff_name = request.POST[uCart.stuffs.name]
                stuff=Stuff.objects.get(name=stuff_name)
                uCart=Cart.objects.get(user=request.user,stuffs=stuff)
                orderlist=Order.objects.create(user=request.user,list=uCart,order_date=order_date)
                orderlist.save()
                subtotal=uCart.quantity*uCart.stuffs.price
                orderlist.subtotal=subtotal
                orderlist.save()

        orderlists=Order.objects.filter(user=request.user)
        pub_times=[]
        orders=[]
        for orderlist in orderlists:
            pub_times.append(orderlist.order_date)
        pub_times=list(set(pub_times))
        for pub_time in pub_times:
            orderlists=Order.objects.filter(order_date=pub_time)
            orders.append(orderlists)
        context={'orderlists':orders,'username':request.user.username,'email':request.user.email}
    else:
        context={'username':request.user.username,'email':request.user.email}
    return  render(request,'mall/info.html',context)