from django.shortcuts import render
from .models import Info
from django.http import HttpResponse
def index(request):
    return HttpResponse("Index Shop")
def contact(request):
    return render(request, 'index.html') 
def info(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '')
        
        info = Info(name=name, email=email, phone=phone, msg=msg)
        info.save()
    return render(request, "myapp/index.html")
