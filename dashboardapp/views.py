from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboardapp/index.html')

def base(request):
    return render(request,'dashboardapp/base.html')