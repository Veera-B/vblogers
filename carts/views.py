from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart
# Create your views here.
def create_cart(user = None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj
def carts_home(request):
    # print(request.session.session_key)
    # print(dir(request.session))
    #request.session['username'] =
    #del request.session['cart_id']
    #cart_id = request.session.get('cart_id',None)
    # if cart_id is None:# and isinstance(cart_id,int):
    #     #print('Create new cart')
    #     #request.session['cart_id'] = request.user.username
    #     cart_obj = create_cart()#Cart.objects.create(user=None)
    #     request.session['cart_id'] = cart_obj.id
    # else:
        #print(('cart is created'))
        #print(cart_id)
    # OR
    # query = Cart.objects.filter(id=cart_id)
    # if query.count() ==1:
    #     cart_obj = query.first()
    #     if request.user.is_authenticated and cart_obj.user is None:
    #             cart_obj.user = request.user
    #             cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id
    #OR
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for product in products:
    #     total += product.price
    #     print(total)
    #     cart_obj.total = total
    #     cart_obj.save()
    context = {
        'cart':cart_obj
    }
    return render(request,'carts/home.html',context)


def cart_update(request):
    id = request.POST.get('product_id')
    #print(id)
    if id is not None:
        try:
            product_obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            print('Product out of stack!')
            return redirect('carts_home')
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

    #return redirect(product_obj.get_absolute_url())
    return redirect('carts_home')
