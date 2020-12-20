
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.item_list , name="item-list")
]