from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"ecomerceapp/home.html")

def electronics_page(request):
    return render(request,"ecomerceapp/Electronics.html")

def clothes_page(request):
    return render(request,"ecomerceapp/clothes.html")

def groceries_page(request):
    return render(request,"ecomerceapp/Groceries.html")
def stationery_page(request):
    return render(request,"ecomerceapp/Stationery.html")
