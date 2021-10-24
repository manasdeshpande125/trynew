from django.http import HttpResponse
from django.shortcuts import render
#username=Manas
#Password=12341234
def index(request):
    return HttpResponse('This is a function based view.')


def about(request):
    return render(request, 'index1.html')
def contact(request):
    return render(request, 'index.html') 