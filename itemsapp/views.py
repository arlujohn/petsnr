from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request,'items/index.html',context)

def addItems(request):
    return render(request,'items/addItems.html')