from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'items': items})

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'myapp/detail.html', {'item': item})

def simple_view(request):
    return HttpResponse("这是一个简单的视图，用于测试应用是否正常工作。")
