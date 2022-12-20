from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def csv_home(request):
    return render(request,'csv/csv_home.html')

def pdf_home(request):
    return render(request,'pdf/pdf_home.html')