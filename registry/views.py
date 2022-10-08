from django.shortcuts import render
from .models import Purchase

def index (request):
    return render(request, "index.html")

def dataTable (request):
    hospital = Purchase.objects.all()
    name = Purchase.objects.all()
    price = Purchase.objects.all()
    signed = Purchase.objects.all()
    returned = Purchase.objects.all()
    transferred = Purchase.objects.all()


    return render(request, "../templates/table/data_table.html", {'hospital': hospital, 'name': name, 'price': price, 'signed': signed, 'returned': returned, 'transferred': transferred})



