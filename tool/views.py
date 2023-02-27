from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from .models import PiplineDetails
import json 


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    
def home(request):
    return render(request,'home.html')

#==========================================DRIVE_HOME=================================================================
current_path=""
localhost="http://localhost:9870/"
def drive_home(request):
    global current_path
    if is_ajax(request=request):
        action = request.GET.get('action')

        if action == "open":
            dir = request.GET.get('button_text')
            if current_path == "":
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+dir+"?op=LISTSTATUS")
                current_path = dir
            else:
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+current_path+"/"+dir+"?op=LISTSTATUS")
                current_path = current_path+"/"+dir
            context = response.json()
            return JsonResponse(context,status=200)
        
        elif action == "back":
            l = current_path.rsplit('/', 1)
            if len(l) <= 1:
                current_path=""
            else:
                current_path=l[0]

            if current_path == "":
                response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
            else:
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+current_path+"?op=LISTSTATUS")
            context = response.json()
            return JsonResponse(context,status=200)
        
        elif action == "new_folder":
            dir_name = request.GET.get('dir_name')
            if current_path == "":
                response = requests.put(localhost+"webhdfs/v1/user/hadoop/"+dir_name+"?user.name=hadoop&op=MKDIRS")
            else:
                response = requests.put(localhost+"webhdfs/v1/user/hadoop/"+current_path+"/"+dir_name+"?user.name=hadoop&op=MKDIRS")


            if current_path == "":
                response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
            else:
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+current_path+"?op=LISTSTATUS")
            context = response.json()
            return JsonResponse(context,status=200)

        elif action == "delete_folder":
            dir_name = request.GET.get('dir_name')
            print(dir_name)
            if dir_name != None:
                if current_path == "":
                    response = requests.delete(localhost+"webhdfs/v1/user/hadoop/"+dir_name+"?user.name=hadoop&op=DELETE&recursive=true")
                else:
                    response = requests.delete(localhost+"webhdfs/v1/user/hadoop/"+current_path+"/"+dir_name+"?user.name=hadoop&op=DELETE&recursive=true")


            if current_path == "":
                response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
            else:
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+current_path+"?op=LISTSTATUS")
            context = response.json()
            return JsonResponse(context,status=200)

        elif action == "copy_current_path":
            data=[]
            data.append("/user/hadoop/"+current_path) 
            return JsonResponse(data, safe=False)

    else:
        current_path=""
        response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
        context = response.json()
        return render(request,'drive/drive_home.html',context)

#==============================CSV_HOME================================================================================
def csv_home(request):
    if is_ajax(request=request):
        action = request.GET.get('action')
        if action == "delete_csv_schedule":
            id = request.GET.get('csv_schedule_id')
            if id != None:
                #delete the Pipline data
                PiplineDetails.objects.filter(id=id).delete()
                
            data = list(PiplineDetails.objects.all().values())
            return JsonResponse(data,safe=False)
    else:
        csv_list = PiplineDetails.objects.values()
        context = {
            'csv_list': csv_list,
        }
        return render(request,'csv/csv_home.html',context)

#==============================COMMON================================================================================
def create(request,file_type):
    if request.method == 'POST':
        if request.POST['piplineName'] != "" and request.POST['fileType'] != "" and request.POST['filePath'] != "" and request.POST['scheduleTime'] != "" and request.POST['tableName'] != "" and request.POST['databaseName'] != "":
            obj = PiplineDetails()
            obj.text = request.POST['piplineName']
            obj.file_type = request.POST['fileType']
            obj.file_path = request.POST['filePath']
            obj.schedule_time = request.POST['scheduleTime']
            obj.table_name = request.POST['tableName']
            obj.database_name = request.POST['databaseName']
            obj.save()
            if request.POST['fileType'] == "CSV":
                return redirect("csv_home")
            else:
                return redirect("pdf_home")
        
        return redirect(request.META['HTTP_REFERER'])  
    else:
        context = {
            'file_type': file_type,
        }
        return render(request,'common/create.html',context)

def edit(request,id):
    if request.method == 'POST':
        if request.POST['piplineName'] != "" and request.POST['fileType'] != "" and request.POST['filePath'] != "" and request.POST['scheduleTime'] != "" and request.POST['tableName'] != "" and request.POST['databaseName'] != "":
            # Pipline_details = PiplineDetails.objects.filter(id=id).values()
        # hive_details = CsvHiveTableDetails.objects.filter(csv_id=Pipline_details["csv_id"]).values()
            # csv_id = models.AutoField(primary_key=True)
            obj = PiplineDetails()
            obj.text = request.POST['piplineName']
            obj.file_type = request.POST['fileType']
            obj.file_path = request.POST['filePath']
            obj.schedule_time = request.POST['scheduleTime']
            obj.table_name = request.POST['tableName']
            obj.database_name = request.POST['databaseName']
            obj.save()
            if request.POST['fileType'] == "CSV":
                return redirect("csv_home")
            else:
                return redirect("pdf_home")
        
        return redirect(request.META['HTTP_REFERER'])  
    else:
        context = {
            'file_type': file_type,
        }
        return render(request,'common/create.html',context)

def hive_edit(request,id):
    context = {
        'csv_list': id,
    }
    return render(request,'common/hive_edit.html',context)

#================================PDF_HOME===============================================================================
def pdf_home(request):
    return render(request,'pdf/pdf_home.html')
 




