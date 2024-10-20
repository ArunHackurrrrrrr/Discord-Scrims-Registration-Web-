from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import os
import math
def index(request):
    # products = Product.objects.all()
    
    

    allProds = []

    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = int(len(prod))
        noSlide = n//4 + math.ceil(n/4 - n//4)
        allProds.append([prod, range(1,noSlide),noSlide])
    param = {'allProds':allProds}


    return render(request,'shop/index.html',param)

def aboutUs(request):
    return render(request , 'shop/about.html')

def contactUs(request):
    return render(request, 'shop/contact.html')

def trackOrder(request):
    return HttpResponse('tracking order')

def search(request):
    return HttpResponse('searching website')

def prodView(requset):
    return HttpResponse('product image / view')

def checkOut(request):
    return HttpResponse('checkout karo and paise doo')

# STEP 1 - GETTING TOTAL NO OF OBJECT INSIDE THE DIR AND MAKING CARD FOR THEM
# STEP 2 - GETTING NAME OF THOSE IMAGES TO SEND TO HTML




# slideMaker(None)