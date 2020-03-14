from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import FoodForm

def index(request):
    item_list = Item.objects.all()
    
    context = {
        'item_list': item_list,
    }
    
    return render(request, 'index.html', context)


def item(request):
    return render(request, 'item.html')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'detail.html', context)


def create_food(request):
    form = FoodForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'food-form.html', {'form': form })

def update_food(request, id):
    item = Item.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'food-form.html', {'form': form, 'item': item })

def delete_food(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('foods:index')
    
    return render(request, 'food-delete.html', {'item': item })    