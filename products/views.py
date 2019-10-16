from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from carts.models import Cart
from .models import Product


#class  based view
#Product List view
class ProductListView(ListView):
    #To get list of objects
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        return context
#Product Detail View
class ProductDetailView(DetailView):
    #To get single object
    model = Product
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    def get_object(self, *args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Not found")
        return instance


    template_name = 'products/detail.html'
    # def get_context_data(self, *args,**kwargs):
    #     context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
#Featured list view cbv
# customized  queries
class ProductFeaturedListView(ListView):
    template_name = 'products/feature.html'
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()
#Featured detail View
class ProductFeaturedDetailView(DetailView):
    template_name = 'products/Featured_detail.html'
    # def get_queryset(self, *args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured() OR
    queryset = Product.objects.all().featured()

class ProductFeaturedSlugDetailView(DetailView):

    template_name = 'products/detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ProductFeaturedSlugDetailView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    #queryset = Product.objects.all()
    def get_object(self,*args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            #instance = Product.objects.get(slug=slug,active=True)
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            #qs = Product.objects.filter(slug=-slug,active=True)
            qs = Product.objects.filter(slug=-slug)
            instance = qs.first()
        except:
            raise Http404("Somthing wrong")
        return instance


#===============================================#
# function based view
def product_list_view(request):
    qs = Product.objects.all()
    context = {
        "product_list":qs
    }
    return render(request,'products/product_list.html',context)
def product_detail_view(request,id):

    #instance = get_object_or_404(Product, pk=id)
    # try:
    #     instance = Product.objects.get(pk=id)
    # except Product.DoesNotExist:
    #     print("No product found")
    #     raise Http404("the product doesnot found")
    # except:
    #     print

    #queryset = Product.objects.get_by_id(id=id)
    instance = Product.objects.get_by_id(id=id)

    #queryset  = Product.objects.filter(pk=id)
    # if queryset.exists() and queryset.count() == 1:
    #     instance = queryset.first()
    #OR
    # if queryset is not None:
    #     instance = queryset
    # else:
    #     raise Http404("Product not found")
    if instance is None:
        raise Http404("Product Not found!")
    context = {
        "object": instance
    }
    return render(request, 'products/detail.html',context)
# Featured view

