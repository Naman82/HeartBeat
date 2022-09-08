from django.shortcuts import render
from .models import User
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')

def registerPage(request):
    return render(request,'register.html')

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
        return render(request,'register.html')

# def doctor(request):
#     if request.method =='POST':
#         username=request.POST['username']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         password=request.POST['password']
#         password2=request.POST['password2']
#         profile=request.FILES['photoInput']
#         state=request.POST['state']
#         city=request.POST['city']
#         pincode=request.POST['pincode']

#         if password == password2 :
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,'Email Already Used')
#                 return redirect('doctor')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request,'Username Already Used')
#                 return redirect('doctor')
#             else:
#                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_doctor=True,profile_pic=profile,state=state,city=city,pincode=pincode)
#                 user.save();
#                 return redirect('doctor_login')

#         else:
#             messages.info(request,'Password does not match , Try again')
#             return redirect('doctor')
#     else:
#         return render(request,'doctor_register.html')

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
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
