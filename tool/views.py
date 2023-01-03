from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


#ajax handler
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.

def home(request):
    return render(request,'home.html')

#drive_home

def drive_home(request):
    if is_ajax(request=request):
        text = request.GET.get('button_text')
        response = requests.get("http://localhost:9870/webhdfs/v1/user/hadoop/"+text+"?op=LISTSTATUS")
        context = response.json()
        return JsonResponse(context,status=200)
    
    response = requests.get("http://localhost:9870/webhdfs/v1/user/hadoop?op=LISTSTATUS")
    context = response.json()
    return render(request,'drive/drive_home.html',context)

def csv_home(request):
    return render(request,'csv/csv_home.html')

def pdf_home(request):
    return render(request,'pdf/pdf_home.html')

#csv
 
def csv_edit(request):
    return render(request,'csv/csv_edit.html')



