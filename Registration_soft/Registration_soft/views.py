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
    scrim_data = dictMaker('Registration_soft/regsoft/NEW_URL_2')
    print(type(scrim_data))
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
    reg_Data = dictMaker('Registration_soft/regsoft/NEW_URL_2')
    i = 0
    n = 0
    scrims = {}
    thread = False
    for item in reg_Data:
        i +=1
        button_Stat = request.POST.get(f'Rvnc_scrim_{i}','off')
         
        scrim_time = reg_Data[f'Rvnc_scrim_{i}']['Time']
        scrim_id = reg_Data[f'Rvnc_scrim_{i}']['id']
        if button_Stat =='on':
            n +=1
            thread = threading.Thread(target= time_check,args=(scrim_time,scrim_id))
            thread.start()
            scrims.update({f'Rvnc_scrim_{n}': f'{scrim_time}'})
    print(scrims.keys())
    return render(request,'registering.html',{"scrims":scrims})
   
 
def registration_pro(scrim_id):
        url = f"https://discord.com/api/v9/channels/{scrim_id}/messages"
    
        headers = {
            "Authorization": "MTExNzgzMzkxODY5NjEyODUxMg.GvYaAS.WztT9Mv0ajNvgZHlnGNh2pzzHzZPRZmoBynSg0",    
            "Content-Type": "application/json"
        }

        msg = {
            'content': 'TEAM NAME : SUGARx <@1117833918696128512> <@896979044837511188> <@1216632380815573035> <@745564134103318539> '
        }

        response = requests.post(url, headers=headers, json=msg)

        print(response.status_code)
        print(response.json())
        a = str(response.status_code )
    
            
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