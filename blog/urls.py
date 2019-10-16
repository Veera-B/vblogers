from django.urls import path
from .views import *


urlpatterns = [
    path('',home_view, name='home_view'),
    path('contact/',contact_view, name="contact"),
    path('login/', login_view, name="login"),
    path('reg/',reg_view, name='register'),
    path('logout/',user_logout,name='logout')
]
