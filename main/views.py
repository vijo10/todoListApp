from django.shortcuts import render,redirect
from.forms import TodoForm,CustomUserCreationForm
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
                if todos.count()==0:
                    messages.warning(request, 'There is no items found in this name')
            else:
                todos = Todo.objects.filter(user=request.user)
            context = {"todos": todos}
            return render(request, "home.html", context)
        else:
            messages.warning(request,"First you have to login")
            return redirect("/")  
        
class Create(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'create.html')
        else:
            messages.warning(request,"You need to log in first")
            return redirect("login") 

    def post(self,request):
        todo_name = request.POST.get("new-todo")
        todo_description = request.POST.get("description")
        todo = Todo.objects.create(title=todo_name, user=request.user,description=todo_description)
        messages.success(request,"You are successfully created new item")
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
            messages.success(request,"You are successfully updated")
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
            messages.success(request,"You successfully deletd one item")
            return redirect("home")
        else:
            messages.warning(request,"You need to log in first")
            return redirect("login")
                


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Registration is completed, Now you can login")
           return redirect('login')   
        return render(request, 'register.html', {'form': form})        

class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("home")
        else:    
            return render(request,"login.html") 
    def post(self,request):
        name=request.POST.get('username')
        passwd=request.POST.get('password')
        user=authenticate(request,username=name.lower(),password=passwd)
        if user is not None:
            if not user.is_superuser:
                login(request,user)
                messages.success(request, f"{request.user.username} you are successfully login")
                return redirect("home")
            else:
                messages.error(request, "Please enter valid credentials",extra_tags='danger')
                return redirect('login')
        else:
          messages.error(request, "Invalid login credentials. Please try again.",extra_tags='danger')
          return render(request, 'login.html')  

class Logout(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request,"Logout successfully")
            return redirect("login") 
        else:
            messages.warning(request,"you are already logout")
            return redirect("login")  
    
