from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ProductForm

# Create your views here.

def get_market_list(request):
    results = Item.objects.all()
    return render(request, "market_list.html", {'items': results})
    
def create_a_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_market_list)
    
    else:
        form = ProductForm()

    return render(request, "product_form.html", {'form': form})
    
def edit_product_values(request, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_market_list)
        else:
            form = ProductForm(instance=item)

    
    form = ProductForm(instance=item)
    return render(request, "product_form.html", {'form': form})


def toggle_product(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_market_list)