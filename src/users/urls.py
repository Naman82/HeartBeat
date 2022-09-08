from django.urls import path
from users import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bloodbank/bloodstock/',views.bloodstock,name='bloodstock'),
    # path('login/',views.loginPage,name='loginPage'),
    # path('register/',views.registerPage,name='registerPage'),
    path('user/register/',views.CustomerRegister,name='customerRegister'),
    path('user/bloodbank/register/',views.BloodBankRegister,name='registerPageBloodBank'),
    path('user/home/',views.CustomerLogin,name='customerLogin'),
    path('user/deliveryperson/register/',views.DeliveryPersonRegister,name='deliveryPersonRegister'),
    path('user/deliveryperson/home/',views.DeliveryPersonLogin,name='deliveryPersonLogin'),
    path('user/bloodbank/stock/',views.BloodBankLogin,name='loginPageBloodBank'),
    path('logout/',views.logout,name='logout'),
]