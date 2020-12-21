
from django.urls import path
from . import views as v

app_name = 'estore'

urlpatterns = [
    path('', v.HomeView.as_view() , name="item-list"),
    path('checkout/',v.checkout , name="checkout"),
    path('product/<slug>/',v.ItemDetailView.as_view() , name='product'),
    path('add-to-cart/<slug>',v.add_to_card , name='add-to-cart'),
    path('remove-from-cart/<slug>',v.remove_from_cart , name='remove-from-cart')
]