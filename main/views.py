from django.shortcuts import render,redirect
from.forms import RegisterForm, TodoForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Todo
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            if 'productsearch' in request.GET:
                productsearch=request.GET['productsearch'] 
                todos = Todo.objects.filter(user=request.user,title__icontains= productsearch)
            else:
                todos = Todo.objects.filter(user=request.user)
            context = {"todos": todos}
            return render(request, "home.html", context)
        else:
            messages.warning(request,"First you have to login")
            return redirect("/")  
    def post(self,request):
        todo_name = request.POST.get("new-todo")
        todo_start = request.POST.get("start")
        todo_end = request.POST.get("end")
        todo = Todo.objects.create(title=todo_name, user=request.user,Start_Time=todo_start,End_Time=todo_end)
        return redirect("home")     

class Update(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            todo=Todo.objects.get(id=id)
            form=TodoForm(instance=todo)
            return render(request,'update.html',{'form':form})
        else:
            messages.warning(request,"You need to log in first")
            return redirect("login") 

    def post(self,request,id):
        todo=Todo.objects.get(id=id)
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

class Delete(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            messages.warning(request,"You need to log in first")
            return redirect("login")
    def post(self,request,id):
        if request.user.is_authenticated:
            Todo.objects.get(id=id).delete()
            return redirect("home")
        else:
            messages.warning(request,"You need to log in first")
            return redirect("login")
                
class Register(View):
    def get(self,request):
        if request.user.is_authenticated:
            messages.warning(request,"If you want create new account first logout your currently loged in account")
            return redirect("home")
        else:
            form=RegisterForm()
            context={'form':form}
        return render(request,'register.html',context)
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.email=user.email.lower()
            user.save()
            login(request,user)
            messages.success(request,"Registration Successfully completed")
            return redirect("login")

class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            messages.warning(request,"you are already login")
            return redirect("home")
        else:    
            return render(request,"login.html") 
    def post(self,request):
        name=request.POST.get('email')
        passwd=request.POST.get('password')
        user=authenticate(request,username=name.lower(),password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Login succeccfully")
            return redirect("home")
        else:
            messages.error(request,"invalid username or password")
            return redirect("login")  

class Logout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,"Logout successfully")
            return redirect("login") 
        else:
            messages.warning(request,"you are already logout")
            return redirect("login")  
    
