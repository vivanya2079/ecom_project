# your_app/urls.py
from django.urls import path
from .views import (
    index, about, shop, mens, womens,
    contact, login_view, order , signup_view, forgot_password_view, logout
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('mens/', mens, name='mens'),
    path('womens/', womens, name='womens'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('order/', order, name='order'),
    path('signup/', signup_view, name='signup'),
    path('forgottpwd/', forgot_password_view, name='forgottpwd'),
    path('logout/', logout, name='logout'),
    
]