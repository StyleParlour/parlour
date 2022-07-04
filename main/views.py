from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Offers

# Create your views here.
def index(request):
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
    return render(request, 'invoice.html')

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
    return render(request, 'otp.html')