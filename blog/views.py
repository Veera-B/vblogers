from django.shortcuts import render, redirect

# Create your views here.
from .forms import ContactForm, LoginForm, RegForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def home_view(request):
    ses_usename=request.session.get('cart_id')
    context = {
        'name':ses_usename
    }
    return render(request,'Home.html',context)

def contact_view(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,'contact.html',context)
def login_view(request):
    login_form = LoginForm(request.POST or None)
    #print(request.user.is_authenticated)
    context = {
        "form" : login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            #context['form'] = LoginForm()
            return  redirect('products')
        else:
            print("ERROR")


    return render(request,'auth/login.html', context)


def reg_view(request):
    reg_form = RegForm(request.POST or None)

    if reg_form.is_valid():
        username = reg_form.cleaned_data.get('username')
        email = reg_form.cleaned_data.get('email')
        password = reg_form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
        #print(reg_form.cleaned_data)

    context = {
        'form' : reg_form
    }
    return  render(request,'auth/reg.html',context)

def user_logout(request):
    if request.user.is_authenticated:
        if logout(request):
            print('logout success!')

    return redirect('products')

