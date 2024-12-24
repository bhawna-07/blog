from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib import messages 
from  django.contrib.auth.models import User
from django.contrib .auth.forms import AuthenticationForm
from django .contrib.auth import authenticate,login ,logout    
from .forms import SignUP ,BlogForm
from .models import BlogModel
 

# Create your views here.


# home page 
def home(request):
    return render(request,'myapp/homepage.html')



def signup_view(request):
    if request.method=='POST':
        fm=SignUP(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm=SignUP()
    return render(request,'myapp/signup.html',{'form':fm})  



def login_view(request):
    if request.method == 'POST':  
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():  
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged  in successfully! 👍')
                return redirect('table')  
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        fm = AuthenticationForm()  
    return render(request, 'myapp/login.html', {'form': fm})



def createblog(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm= BlogForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm=BlogForm()
        else:
            fm=BlogForm()
        return render(request,'myapp/createblog.html',{'form':fm})      
    else:
        return redirect('login')
    
    
    
def blog_table(request):
    if request.user.is_authenticated:
        blog=BlogModel.objects.all()
    else:
        return redirect('login')
    return render(request,'myapp/blogtable.html',{'blog':blog}) 





def blog_detail(request, id):
    if request.user.is_authenticated:
        detail = get_object_or_404(BlogModel, pk=id)
    else:
        return redirect('login')  
    return render(request, 'myapp/detail.html', {'detail': detail})



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    
    
    
    
def blog_update(request, id):
  if request.user.is_authenticated: 
     pi = BlogModel.objects.get(pk=id)
     if request.method == 'POST':
        fm = BlogForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
     else:
        fm = BlogForm(instance=pi)
    
     return render(request, 'myapp/update.html', {'form': fm, 'pi': pi})

  else :
      return redirect('login') 






def delete_data(request, id):
    if request.method == 'POST':
        try:
            pi = BlogModel.objects.get(pk=id) 
            pi.delete() 
            return redirect('table')  
        except BlogModel.DoesNotExist:
            return redirect('table')
    
    return redirect('table')


            

          
          
     

    
       
            

                    
        
               
                 

       
         


 



