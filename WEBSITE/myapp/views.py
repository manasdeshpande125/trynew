from django.shortcuts import render
from .models import Blogpost, Info
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Shop")
def contact(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '')
        
        info = Info(name=name, email=email, phone=phone, msg=msg)
        info.save()

    return render(request, "index.html")
    #return render(request, 'index.html') 
def blog(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request,'basic.html',{'post':post})

def index1(request):
    myposts= Blogpost.objects.all()
    #print(myposts)
    return render(request, 'final.html', {'myposts': myposts})
