from django.shortcuts import render
from .models import User,BloodStock
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
import stripe


stripe.api_key = 'sk_test_51LgXo0SEd9yZ4TiMmUSXBYmkghXBR0WXgHFlJtNYFBlumqwxdaaEqEU28Jvt8QcbQyyMkdWc9IY8zh6MI9oMKdcR00vrptacHj'

# Create your views here.
def index(request):
    return render(request,'index.html')

# def bloodStock(request):
#     if request.POST:
#         apositive = request.POST['A_positive']
#         anegative = request.POST['A_negative']
#         opositive = request.POST['O_positive']
#         onegative = request.POST['O_negative']
#         abpositive = request.POST['AB_positive']
#         abnegative = request.POST['AB_negative']

#         new_bloodstock = BloodStock(user=request.user,apositive=apositive,anegative=anegative,onegative=onegative,opositive=opositive,abnegative=abnegative,abpositive=abpositive)
#         new_bloodstock.save()
#         return redirect('index')
#     return render(request,'bloodbank/bloodstock.html')

def bloodStockEdit(request,pk):
    if pk is not None:
        
        if request.POST:
            user=User.objects.get(pk=pk)
            update_bloodstock=BloodStock.objects.get(user=user)
            apositive = request.POST['A_positive']
            anegative = request.POST['A_negative']
            opositive = request.POST['O_positive']
            onegative = request.POST['O_negative']
            abpositive = request.POST['AB_positive']
            abnegative = request.POST['AB_negative']

            update_bloodstock.apositive=apositive
            update_bloodstock.anegative=anegative
            update_bloodstock.opositive=opositive
            update_bloodstock.onegative=onegative
            update_bloodstock.abpositive=abpositive
            update_bloodstock.abnegative=abnegative

            # new_bloodstock = BloodStock(user=request.user,A_positive=A_positive,A_negative=A_negative,O_negative=O_negative,O_positive=O_positive,AB_negative=AB_negative,AB_positive=AB_positive)
            update_bloodstock.save()
            return redirect('index')
        else:
            return render(request,'bloodbank/bloodstockedit.html')
    return render(request,'bloodbank/bloodstock.html')

def CustomerRegister(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('registerPage')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('registerPage')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_customer=True)
                user.save();
                return redirect('loginPage')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('registerPage')
    else:
        return render(request,'customer/register.html')



def CustomerLogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_customer==True:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('loginPage')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('loginPage')
    else:
        return render(request,'customer/login.html')


def BloodBankRegister(request):
    if request.method =='POST':
        # username=request.POST['username']
        first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('registerPageBloodBank')
            # elif User.objects.filter(username=username).exists():
            #     messages.info(request,'Username Already Used')
            #     return redirect('registerPage')
            else:
                user=User.objects.create_user(username=email,first_name=first_name,email=email,password=password,is_bloodbank=True)
                user.save();
                return redirect('loginPageBloodBank')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('registerPageBloodBank')
    else:
        return render(request,'bloodbank/registerBloodBank.html')

def BloodBankLogin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=email,password=password)

        if user is not None:
            if user.is_bloodbank==True:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('loginPageBloodBank')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('loginPageBloodBank')
    else:
        return render(request,'bloodbank/loginBloodBank.html')

def DeliveryPersonRegister(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('deliveryPersonRegister')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('deliveryPersonRegister')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_deliveryPerson=True)
                user.save();
                return redirect('deliveryPersonLogin')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('deliveryPersonRegister')
    else:
        return render(request,'deliveryPerson/register.html')

def DeliveryPersonLogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_deliveryPerson==True:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('deliveryPersonLogin')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('deliveryPersonLogin')
    else:
        return render(request,'deliveryPerson/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def BloodBankList(request):
    bloodbanks=BloodStock.objects.all()
    # print(bloodbanks)
    return render(request,'bloodbank/bloodbanklist.html',{'bloodbanks':bloodbanks})

def BloodOrder(request,pk):
    bloodbank=BloodStock.objects.get(pk=pk)
    # print(bloodbank.user.first_name)
    return render(request,'bloodbank/orderAmount.html',{'bloodbank':bloodbank})

def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')


YOUR_DOMAIN = 'http://localhost:8000'

def paymentPage(request):
    if request.method == 'POST':
        quantity = request.POST['quantity']
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LgfIfSEd9yZ4TiMcl4DMWS1',
                    'quantity': quantity,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    return redirect(checkout_session.url, code=303)