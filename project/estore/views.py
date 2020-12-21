from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView , DetailView
from .models import Item , OrderItem , Order
from django.utils import timezone
from django.contrib import messages


class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


def checkout(request):
    return render(request , 'checkout-page.html')

def add_to_card(request , slug):
    item = get_object_or_404(Item , slug=slug)
    order_item  , created = OrderItem.objects.get_or_create(item=item,
                                                user=request.user ,
                                                ordered=False
                                                )
    order_qs = Order.objects.filter(user=request.user ,
                                    ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            messages.info(request , f"The {item.title} quantity was updated to you cart")
            order_item.save()
            return redirect("estore:product" ,slug=slug)
        else:
            messages.info(request , f"The {item.title} was added to you cart")
            order.items.add(order_item)
            return redirect("estore:product" ,slug=slug)
    else:
        ordered_date = timezone.now()
        order= Order.objects.create(user=request.user , ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request , f"The {item.title} was added to you cart")
        return redirect("estore:product" ,slug=slug)


def remove_from_cart(request , slug):
    item = get_object_or_404(Item , slug=slug)
    order_qs = Order.objects.filter(user=request.user ,
                                    ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                user=request.user ,
                                                ordered=False
                                                )[0]
            order.items.remove(order_item)
            messages.info(request , f"The {item.title} was removed from your cart")
            return redirect("estore:product" ,slug=slug)
        else:
            messages.info(request , f"The {item.title} was not in your cart")
            return redirect("estore:product" ,slug=slug)
    else:
        messages.info(request , f"you do not have an active order")
        return redirect("estore:product" ,slug=slug)


