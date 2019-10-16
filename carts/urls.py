from django.urls import path

from .views import carts_home,cart_update

urlpatterns = [
    path('',carts_home ,name="carts_home"),
    path('update/',cart_update ,name="update"),
]
