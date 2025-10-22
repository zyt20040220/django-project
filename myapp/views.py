from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'items': items})

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'myapp/detail.html', {'item': item})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'myapp/create_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detail', item_id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp/edit_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'myapp/delete_item.html', {'item': item})

def simple_view(request):
    return HttpResponse("这是一个简单的视图，用于测试应用是否正常工作。")
