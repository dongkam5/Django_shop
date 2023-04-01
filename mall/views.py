from django.shortcuts import render,get_object_or_404,redirect
from .models import Stuff,Cart
from .forms import StuffForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
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
        stuff.pub_date=timezone.now()
        stuff.save()
        return redirect('mall:index')
    else:
        form=StuffForm()
        return render(request,'mall/register.html',{'form':form})

@login_required(login_url='common:login')
def info(request):
    email=request.user.email
    username=request.user.username
    context={'username':username,'email':email}
    return render(request,'mall/info.html',context)

@login_required(login_url='common:login')
def cart(request):
    if Cart.objects.filter(pk=request.user.id):
        order=Cart.objects.get(pk=request.user.id)
        stuffs=order.stuffs.all()
        context={'stuffs':stuffs}
    else:
        context={'stuffs':''}
    return render(request,'mall/cart.html',context)

@login_required(login_url='common:login')
def addCart(request,stuff_id):
    if Cart.objects.filter(pk=request.user.id):
        thisCart=Cart.objects.get(pk=request.user.id)
    else:
        thisCart=Cart.objects.create(user=request.user,pk=request.user.id)
    # stuff=Stuff.objects.get(id=stuff_id) 
    stuff=thisCart.stuffs.get(id=stuff_id)
    stuff.quantity+=1
    stuff.save()
    thisCart.stuffs.add(stuff)
    thisCart.save()
    return  redirect('mall:cart')