import ast
import time
import requests
import datetime
import threading
from django.http import HttpResponse
from django.shortcuts import render
i =0
def index(request):
    return render(request,'index.html')
def registration(request):
    from Registration_soft.models import ScrimsData
    scrim_data = ScrimsData.objects.all()
    return render(request,'registration_ui.html',{"scrim_data": scrim_data})


def dictMaker(fileName):
    with open(f'{fileName}.txt','r') as dictData:
        dictReadData = dictData.read().strip()
        dictReadData2 = f"({dictReadData})"
        convOne = dictReadData2.replace("(","{")
        convTwo = convOne.replace(")","}")
        dictReadDataConv = ast.literal_eval(convTwo)
        return dictReadDataConv

def registration_Starter(request):
    from Registration_soft.utils.time_check import time_check
    from Registration_soft.models import ScrimsData
   
    print('infun')
    scrims = {}
    scrims_data = ScrimsData.objects.all()

    for data in scrims_data:
        button_Stat = request.POST.get(f'{data.ScrimsId}','off')
        print(data.ScrimsId)
        
        if button_Stat == 'on':
            print('init')
            thread = threading.Thread(target=time_check,args=(data.ScrimsRegTime,data.ScrimsId))
            thread.start()
            scrims.update({ f'{data.ScrimsName}': f'{data.ScrimsTime}'})
            
            from Registration_soft.utils.Scrims_Data_auto import auto_data

            auto_data(data.ScrimsName,data.ScrimsId,data.ScrimsTime)
            

    print(scrims.keys())
    return render(request,'registering.html',{"scrims":scrims})

    
            
def update_Data(request):
     return render(request,'Scrim_Data.html')


def AddData(request):
    from Registration_soft.utils.UpdateData import AddNewData
    AddNewData(request)
    

    return render(request, 'Scrim_Data.html')

def AuthCheck(request):
    from Registration_soft.utils.UpdateData import OneTimeData
    OneTimeData(request)
    return render(request,'auth_noti.html')

def PerfManage(request):
    return render(request, 'performance.html')