from django.shortcuts import render
from .models import User
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def bloodstock(request):
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
        first_name=request.POST['bloodbank_name']
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
                return redirect('bloodstock')
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
