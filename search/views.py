from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.
from products.models import Product


class SearchProducts(ListView):
    #queryset = Product.objects.all()
    template_name = 'search/search.html'
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProducts,self).get_context_data(*args,**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    def get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q')
        if query is not None:
            #lookups = Q(product_name__icontains=query) | Q(description__icontains=query)|Q(price__icontains=query)
            #return Product.objects.filter(lookups).distinct()
            return Product.objects.search(query)
        return Product.objects.featured()

