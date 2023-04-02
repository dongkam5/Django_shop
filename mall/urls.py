"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path, include
app_name='mall'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:stuff_id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('info/',views.info,name='info'),
    path('cart/',views.cart,name='cart'),
    path('cart/<int:stuff_id>/add',views.addCart,name='addcart'),
    path('cart/<int:stuff_id>/delete',views.subCart,name='subCart'),
    path('cart/<int:stuff_id>/plus',views.plusStuff,name='plusStuff'),
    path('cart/<int:stuff_id>/minus',views.minusStuff,name='minusStuff'),
    path('buy/<int:stuff_id>/',views.buyAtIndex,name='buyAtIndex'),
]
