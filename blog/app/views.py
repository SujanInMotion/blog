from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from app.forms import UserForm,BlogsForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog

# Create your views here.

#@login_required
def home(request):
    blog_obj = Blog.objects.all() 
    data = {"blogs":blog_obj}
    return render(request,"index.html",context = data)
    



@login_required
def create_blog(request):
    create_blog_obj = BlogsForm()
    data = {'form':create_blog_obj}
    if request.method == "POST":
        create_blog_obj = BlogsForm(data=request.POST)
        if create_blog_obj.is_valid():
            create_blog_obj.save()
            messages.success(request,"Blog created Sucessfully")
            #return render(request,"create_blog.html", context= data)
            return redirect('home')
            
            
        else:
            messages.error(request,create_blog_obj.errors)
            return render(request,"create_blog.html",context=data)    
    return render(request,"create_blog.html",context=data)    


     


@login_required
def edit_blog(request,pk):
    pass













def signup(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hash_password = make_password(password)
        data = request.POST.copy()
        data['password']= hash_password
        user_form_obj = UserForm(data=data)
        if user_form_obj.is_valid():
            user_form_obj.save()
            return redirect('login')
    user_form_obj = UserForm()
    data = {'form':user_form_obj}
    return render(request,'signup.html',context=data)


def user_login(request):    
    if request.method == 'POST':
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')
        
        user = authenticate(username=user_username,password=user_password)
        
        if user != None:            
            login(request,user)
            return redirect('home')
    
    user_form_obj = UserForm()
    data = {'form':user_form_obj}
    return render(request,'login.html',context=data)

    

@login_required
def profile(request):
    pass



@login_required
def delete(request,pk):
    delte_obj = Blog.objects.get(id=pk)
    delte_obj.delete()
    return redirect(home)



def logoutView(request):    
    logout(request)
    return redirect(home)

def modify(request):
    pass