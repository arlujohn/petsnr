from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required # - Special functions that modify other functions - Triggers other functions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .form import ItemsForm, RegistrationForm
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


#MAIN ITEMS

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect(homepage_view)
        else:
            form = RegistrationForm()
            return render(request,'accounts/register.html',{'form':form})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request,'accounts/login.html',{'error':error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    

# Home View
# Using the decorator
@login_required
def homepage_view(request):
    return render(request,'auth1_app/home.html')

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request,'registration/protected.html')



