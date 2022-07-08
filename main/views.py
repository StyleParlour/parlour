import imp
from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Offers, Customers, Service, Slot, Booking
from uuid import uuid4
import random
from django.core.mail import send_mail  

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        token = random.randint(1000, 9999)
        customer = Customers(name=name, email=email, phone=phone, token=token)
        customer.save()
        send_mail('OTP', 'Your OTP is ' + str(token), 'hairnationparlour@gmail.com', [email])
        return redirect('/otp/')
    return render(request, 'index.html')

def analytics(request):
    return render(request, 'analytics.html')

def offers(request):
    if request.method =="POST":
        ccode = request.POST['ccode']
        cdesc = request.POST['cdesc']
        poff = request.POST['poff']
        offer = Offers(code=ccode, name=cdesc, percentOff=poff)
        offer.save()
    
    codes = Offers.objects.all()
    param = {'codes': codes}
    return render(request, 'offers.html', param)

def frequency(request):
    return render(request, 'frequency.html')

def invoice(request):
    bookings = Booking.objects.all()
    print(bookings)
    param = {'bookings': bookings}
    return render(request, 'invoice.html', param)

def slots(request):
    return render(request, 'slots.html')

def products(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        brandName = request.POST['brandName']
        currentStock = request.POST['currentStock']
        image = request.FILES['image']
        product = Product(name=name, price=price, brandName=brandName, currentStock=currentStock, image=image)
        product.save()    

    products = Product.objects.all()
    param = {'products': products}   
    return render(request, 'addpro.html', param)

def delete(request, id):
    offer = Offers.objects.get(oId=id)
    offer.delete()
    return redirect('/admin/offers/')

def deletePro(request, id):
    product = Product.objects.get(pId=id)
    product.delete()
    return redirect('/admin/products/')

def shop(request):
    prods = Product.objects.all()
    param = {'prods': prods}
    return render(request, 'shop.html', param)

def slot(request):
    return render(request, 'slot.html')

def otp(request):
    slots = Slot.objects.all()
    Services = Service.objects.all()
    if request.method == 'POST':
        otp = request.POST['otp']
        slot = request.POST['date']
        service = request.POST['service']
        customer = Customers.objects.get(token=otp)
        if customer:
            slot = Slot.objects.get(sId=slot)
            service = Service.objects.get(sId=service)
            booking = Booking(customer=customer, slot=slot, service=service)
            booking.save()
            slot.slotRemaining = slot.slotRemaining - 1
            slot.save()
            send_mail('Booking', 'Your booking is confirmed', 'hairnationparlour@gmail.com', [customer.email])
            return redirect('/')
    param = {'slots': slots, 'Services': Services}

    return render(request, 'otp.html', param)

def invoiceGen(request, id):
    booking = Booking.objects.get(bId=id)
    param = {'booking': booking}
    return render(request, 'invoiceTemp.html',param)