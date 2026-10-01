from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ItemsForm
from .models import Item

# Create your views here.

#This is the home page view function
def home_view(request):
    return render(request,'items/home.html')

def items_display(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request,'items/displayItems.html',context)


# Define the add items function to handle the items form
def addItems(request):
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.add_items()
            return redirect(adding_items_success)
    else:
        form = ItemsForm()

    context = {'form':form}
    return render(request,'items/addItems.html',context)


# Define the adding-items-success view
def adding_items_success(request):
    return render(request,'items/addItemsSuccess.html')






