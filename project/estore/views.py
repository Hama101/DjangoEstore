from django.shortcuts import render
from .models import Item , OderItem , Order

# Create your views here.
def home(request):
    return render(request , 'base.html')

def item_list(request):
    items = Item.objects.all()
    context={
        "items" : items ,
    }
    return render(request , 'item_list.html',context)