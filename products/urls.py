from django.urls import path

from .views import (
                    #product_list_view,
                    ProductListView,
                    # product_detail_view,
                    # ProductDetailView,
                    # ProductFeaturedListView,
                    # ProductFeaturedDetailView,
                    ProductFeaturedSlugDetailView)

#app_name = 'products' NOT WORKING
urlpatterns = [
    path('',ProductListView.as_view(),name="products"),
    # path('prodfbv/',product_list_view,name="prod_fbv"),
    # path('<int:pk>/cvd_prod/',ProductDetailView.as_view(),name="cvd_prod"),
    # path('<int:id>/fnv_details/',product_detail_view,name='fnv_detail'),
    # path('pflvc/',ProductFeaturedListView.as_view(),name="pflvc"),
    # path('<int:pk>/pflvc/',ProductFeaturedDetailView.as_view(),name='pflvc'),
    path('<slug:slug>/',ProductFeaturedSlugDetailView.as_view(),name='slug_view')
]
