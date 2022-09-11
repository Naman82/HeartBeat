from django.urls import path
from users import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('bloodbank/bloodstock/',views.bloodStock,name='bloodStock'),
    path('bloodbank/bloodstock/edit/<pk>',views.bloodStockEdit,name='bloodStockEdit'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),
    path('user/register/',views.CustomerRegister,name='customerRegister'),
    path('user/bloodbank/register/',views.BloodBankRegister,name='registerPageBloodBank'),
    path('user/home/',views.CustomerLogin,name='customerLogin'),
    path('user/deliveryperson/register/',views.DeliveryPersonRegister,name='deliveryPersonRegister'),
    path('user/deliveryperson/home/',views.DeliveryPersonLogin,name='deliveryPersonLogin'),
    path('user/bloodbank/login/',views.BloodBankLogin,name='loginPageBloodBank'),
    path('user/bloodbank/list/',views.BloodBankList,name='bloodBankList'),
    path('user/bloodbank/order/<pk>',views.BloodOrder,name='orderAmount'),
    path('logout/',views.logout,name='logout'),
    path('create-checkout-session/',views.paymentPage,name='paymentPage'),
]