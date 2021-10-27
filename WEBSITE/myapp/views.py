from django.shortcuts import render
from .models import Blogpost, Info
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,  login, logout
from django.views.decorators.csrf import csrf_exempt



def index(request):
    #return HttpResponse('Blog page')
    return render(request,"my.html")
def contact(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '')
        
        #info = Info(name=name, email=email, phone=phone, msg=msg)
        #info.save()
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(msg)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            info=Info(name=name, email=email, phone=phone, msg=msg)
            info.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, "index.html")
    #return render(request, 'index.html') 
def blog(request,id):
    
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request,'basic.html',{'post':post})
    
        

def index1(request):
    myposts= Blogpost.objects.all()
    #print(myposts)
    return render(request, 'final.html', {'myposts': myposts})

def blogPost(request, slug): 
    return HttpResponse(f'This is blogPost : {slug}')

@csrf_exempt
def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('myapp')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('myapp')

        if User.objects.filter(username=username).exists():
            if (pass1!= pass2):
                #if User.objects.filter(username=username).exists():
                messages.error(request, " Passwords do not match")
                return redirect('myapp')
        else:
             messages.error(request, " Username already Exists")

        #myuser = User.objects.create_user(username=username, email=email,fname=fname,lname=lname, pass1=pass1,apss2=pass2)
        #myuser.first_name= fname
        #myuser.last_name= lname
        #myuser.save()
        #messages.success(request, " Your iCoder has been successfully created")
        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('myapp')

    else:
        return HttpResponse("404 - Not found")
@csrf_exempt
def handleLogin(request):
    #return HttpResponse("login")


    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=auth.authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('myapp')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('myapp')

    return HttpResponse("404- Not found")

def handleLogout(request):
    #return HttpResponse("logout")
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('myapp')
