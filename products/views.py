from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import products
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    obj=products.objects.all()
    data={
        'products':obj

    }
    return render(request,'index.html',data)

@login_required
def add_product(request):
    data={}
    try:
        if request.method=="POST":
              name=request.POST.get('name')
              price=request.POST.get('price')
              quantity=request.POST.get('quantity')
              description=request.POST.get('description')
              image=request.FILES.get('image')
              bill=request.FILES.get('bill')
              obj=products(
                    name = name,
                    price=price,
                    quantity=quantity,
                    description=description,
                    image=image,
                    bill=bill,
              )
              obj.save()
              return redirect('Home')
    except Exception as e:
         print("error:" ,e)
    return render(request,'add.html')

@login_required
def del_product(request,id):
     obj=products.objects.get(id=id)
     obj.delete()
     return redirect('Home')

@login_required    
def update_product(request,id):
    obj=products.objects.get(id=id)
    try:
         
        if request.method == "POST":
            obj.name = request.POST.get('name')
            obj.price = request.POST.get('price')
            obj.quantity = request.POST.get('quantity')
            obj.description = request.POST.get('description')

            bill = request.FILES.get('bill')
            if bill:
             obj.bill = bill

            image = request.FILES.get('image')
            if image:
             obj.image = image

            obj.save()
            return redirect('Home')
    except Exception as e:
         print("error:" ,e)
    return render(request,'update.html',{'products': obj})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages 

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password")  

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          confirm_password = request.POST.get('confirm_password')

          if password != confirm_password:
               messages.error(request, "Password does not match")
               return redirect('register')
          if User.objects.filter(username=username).exists():
               messages.error(request, "Username already exists")
               return redirect('register')
          
          User.objects.create_user(username=username , password=password)
          messages.success(request,"Account created successfully")
          return redirect('login')
    
    return render(request,'register.html')
            

