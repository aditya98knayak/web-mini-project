from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'initial.html')
def login(request):
    return render(request,'dashboard.html')