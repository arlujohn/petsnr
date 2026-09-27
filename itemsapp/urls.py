from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.home_view,name='Home'),
    path('items', views.items_display,name='displayitems'),
    path('addItems', views.addItems,name='addItems'),
    path('success', views.adding_items_success,name='addItemsSuccess'),
]

