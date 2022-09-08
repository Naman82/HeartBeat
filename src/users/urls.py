from django.urls import path
from users import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.loginPage,name='loginPage'),
    path('register/',views.registerPage,name='registerPage'),
    path('user/register/',views.CustomerRegister,name='customerRegister'),
    path('user/home/',views.CustomerLogin,name='customerLogin'),
]