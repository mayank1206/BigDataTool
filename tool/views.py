from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .models import CsvPipline

#ajax handler
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.

def home(request):
    return render(request,'home.html')

#==========================================DRIVE_HOME=================================================================
current_path=""
localhost="http://localhost:9870/"
def drive_home(request):
    global current_path
    if is_ajax(request=request):
        action = request.GET.get('action')

        #Open Folder
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
        
        #back Button
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
            if dir_name != None:
                print(dir_name)
                if current_path == "":
                    response = requests.put(localhost+"webhdfs/v1/user/hadoop/"+dir_name+"?user.name=hadoop&op=DELETE&recursive=true")
                else:
                    response = requests.put(localhost+"webhdfs/v1/user/hadoop/"+current_path+"/"+dir_name+"?user.name=hadoop&op=DELETE&recursive=true")


            if current_path == "":
                response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
            else:
                response = requests.get(localhost+"webhdfs/v1/user/hadoop/"+current_path+"?op=LISTSTATUS")
            context = response.json()
            return JsonResponse(context,status=200)

    else:
        current_path=""
        response = requests.get(localhost+"webhdfs/v1/user/hadoop?op=LISTSTATUS")
        context = response.json()
        return render(request,'drive/drive_home.html',context)

#==============================CSV_HOME================================================================================
def csv_home(request):
    print("test")
    if is_ajax(request=request):
        action = request.GET.get('action')

        if action == "new_csv_schedule":
            name = request.GET.get('csv_schedule_name')
            obj = CsvPipline()
            obj.text = name
            obj.save()
            data = list(CsvPipline.objects.all().values())
            return JsonResponse(data,safe=False)

        elif action == "delete_csv_schedule":
            id = request.GET.get('csv_schedule_id')
            if id != None:
                CsvPipline.objects.filter(id=id).delete()
                #delete the pipline 
            data = list(CsvPipline.objects.all().values())
            return JsonResponse(data,safe=False)
            
    else:
        csv_list = CsvPipline.objects.values()
        context = {
            'csv_list': csv_list,
        }
        return render(request,'csv/csv_home.html',context)


def csv_edit(request,id):

    return render(request,'csv/csv_edit.html')

#================================PDF_HOME===============================================================================
def pdf_home(request):
    return render(request,'pdf/pdf_home.html')
 




