from django.shortcuts import render,HttpResponse
from .models import Item

# Create your views here.

def get_market_list(request):
    results = Item.objects.all()
    return render(request, "market_list.html", {'items': results})