from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def Indexpage(request):
   return render(request,"app/index.html")
def Signup(request):
      if request.method=="POST":
         username=request.POST['username']
         firstname=request.POST['firstname']
         lastname=request.POST['lastname']
         email=request.POST['email']
         password=request.POST['password']
         cpassword=request.POST['cpassword']


         myuser=User.objects.create_user(username=username,email=email,password=password)

         myuser.firstname=firstname
         myuser.lastname=lastname

         myuser.save()
         messages.info(request,"your account has been sucessfully created")
         return redirect('signin')
      
      return render(request,"app/signup.html")

         
def Signout(request):
   return render(request,"app/signout.html")
   
def Signin(request):
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']

      user=authenticate(username=username,password=password)
      print(user.is_authenticated)
      if user is not None:
         login(request,user)
         firstname=User.firstname
         return render(request,"app/index.html",{'firstname':firstname})
      else:
         messages.error(request,"wrong credietials")
         return redirect('index')
   return render(request,"app/signin.html")