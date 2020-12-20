
from django.urls import path
from . import views as v

app_name = 'estore'

urlpatterns = [
    path('', v.HomeView.as_view() , name="item-list"),
    path('checkout/',v.checkout , name="checkout"),
    path('product/<slug>/',v.ItemDetailView.as_view() , name='product'),
]