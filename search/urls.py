from django.urls import path

from .views import SearchProducts

urlpatterns = [
    path('',SearchProducts.as_view(),name="search")
]
