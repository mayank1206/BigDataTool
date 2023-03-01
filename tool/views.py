from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from .models import PiplineDetails, HiveTableDetails
import json 
import os
import csv


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    return render(request,'home.html')

def create_csv(id,path):
    os.system("rm /home/hadoop/project/BigDataTool/tool/hold/*")
    os.system("hdfs dfs -get "+path+"/* /home/hadoop/project/BigDataTool/tool/hold/")
    file_name = os.listdir("/home/hadoop/project/BigDataTool/tool/hold/")
    
    with open("/home/hadoop/project/BigDataTool/tool/hold/"+file_name[0], mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            header = lines
            break
    for name in header:
        obj = HiveTableDetails()
        obj.file_id = id
        obj.column_name = name
        obj.file_column_name = name
        obj.save()



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

def hive_csv(id):
    pipline_details = PiplineDetails.objects.filter(id=id).values()
    for pipline_detail in pipline_details:
        table_name =  pipline_detail["table_name"]
        file_path =   pipline_detail["file_path"]
        schedule_time =   pipline_detail["schedule_time"]

    #hive command
    unique_name = table_name+"_"+str(id)
    hive_file = "/home/hadoop/project/BigDataTool/tool/temp_file/hive/"+unique_name+".hive"
    
    create_command= "DROP TABLE IF EXISTS "+table_name+"; create table "+table_name+"( "
    hive_columns = HiveTableDetails.objects.filter(file_id=id).values()
    column_list=[]
    for hive_column in hive_columns:
        column_list.append(hive_column["file_column_name"])
        column = hive_column["column_name"].replace(" ", "_")
        create_command = create_command+column+" string, "
    
    create_command = create_command[:-2]+") row format delimited fields terminated by ',';"

    with open(hive_file, mode="w", encoding="utf-8") as file:
        file.write(create_command)

    os.system("hive -f "+hive_file)	
    
    # write multiple line code in python
    python_file = "/home/hadoop/project/BigDataTool/tool/temp_file/script/"+unique_name+".py"
    staging_area = "/home/hadoop/project/BigDataTool/tool/temp_file/stagging/"
    with open(python_file, mode="w", encoding="utf-8") as file:
        file.write('import os\n')
        file.write('import pandas as pd\n')
        file.write('os.system("rm '+staging_area+'*")\n')
        file.write('os.system("hdfs dfs -get '+file_path+'/* '+staging_area+'")\n')
        file.write('os.system("hdfs dfs -rm '+file_path+'/*")\n')
        file.write('file_name = os.listdir("'+staging_area+'")\n')
        file.write('input_file = pd.read_csv("'+staging_area+'"+file_name[0])\n')
        file.write('output_data = input_file['+str(column_list)+']\n')
        file.write('output_df = pd.DataFrame(output_data)\n')
        file.write('output_df.to_csv("'+staging_area+'"+file_name[0], index=False,header=False)\n')
        file.write('os.system("hdfs dfs -put '+staging_area+'* /user/hive/warehouse/'+table_name+'")\n')
    
    #cron job
    os.system('crontab -r')
    pipline_details = PiplineDetails.objects.values()
    cronjobs=""
    for pipline_detail in pipline_details:
        id =   pipline_detail["id"]
        table_name =  pipline_detail["table_name"]
        schedule_time =   pipline_detail["schedule_time"]
        cronjobs += schedule_time+" python3 /home/hadoop/project/BigDataTool/tool/temp_file/script/"+table_name+"_"+str(id)+".py"
        os.system('(crontab -l 2>/dev/null; echo "'+cronjobs+'") | crontab -')
    

#==============================COMMON================================================================================
def create(request,file_type):
    if request.method == 'POST':
        if request.POST['piplineName'] != "" and request.POST['fileType'] != "" and request.POST['filePath'] != "" and request.POST['scheduleTime'] != "" and request.POST['tableName'] != "":
            obj = PiplineDetails()
            obj.text = request.POST['piplineName']
            obj.file_type = request.POST['fileType']
            obj.file_path = request.POST['filePath']
            obj.schedule_time = request.POST['scheduleTime']
            obj.table_name = request.POST['tableName']
            obj.save()
            
            if request.POST['fileType'] == "CSV":
                create_csv(obj.pk,request.POST['filePath'])
                return redirect("csv_home")
            else:
                #create_pdf
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
            PiplineDetails.objects.filter(id=request.POST['piplineId']).update(text = request.POST['piplineName'] ,file_path = request.POST['filePath'] , schedule_time = request.POST['scheduleTime'] , table_name = request.POST['tableName'], database_name = request.POST['databaseName'])
            #edit process
            if request.POST['fileType'] == "CSV":
                return redirect("csv_home")
            else:
                return redirect("pdf_home")
        return redirect(request.META['HTTP_REFERER'])
    else:
        pipline_details = PiplineDetails.objects.filter(id=id).values()
        context = {
            'pipline_details': pipline_details,
        }
        return render(request,'common/edit.html',context)


def hive_edit(request,id):
    if is_ajax(request=request):
        action = request.GET.get('action')

        if action == "update_column":
            column_id = int(request.GET.get('column_id'))
            HiveTableDetails.objects.filter(id=column_id).update(column_name = request.GET.get('new_name'))

            data = list(HiveTableDetails.objects.filter(file_id=int(request.GET.get('id'))).values())
            return JsonResponse(data,safe=False)

        elif action == "remove_column":
            column_id = int(request.GET.get('column_id'))
            HiveTableDetails.objects.filter(id=column_id).delete()

            data = list(HiveTableDetails.objects.filter(file_id=int(request.GET.get('id'))).values())
            return JsonResponse(data,safe=False)

        elif action == "hive_csv":
            hive_csv(int(request.GET.get('id')))
            data = ["success"]
            return JsonResponse(data,safe=False)

        elif action == "pdf_csv":
            # pdf_csv(int(request.GET.get('id')))
            data = ["success"]
            return JsonResponse(data,safe=False)
        
    else:
        hive_column_details = HiveTableDetails.objects.filter(file_id=id).values()
        context = {
            'hive_column_details': hive_column_details,
            'id':id,
        }
        return render(request,'common/hive_edit.html',context)

#================================PDF_HOME===============================================================================
def pdf_home(request):
    return render(request,'pdf/pdf_home.html')
 




