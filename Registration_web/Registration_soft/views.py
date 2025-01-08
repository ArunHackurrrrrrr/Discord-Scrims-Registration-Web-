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
    from Registration_soft.models import Auto_save_Data
    data = Auto_save_Data.objects.all()
    return render(request, 'performance.html',{"PerfData":data})

def perfIN(request):
    if request.method == 'POST':
        btnID = request.POST.get('action')
        from Registration_soft.models import Auto_save_Data
        from Registration_soft.models import OneTimeDatas 
        pdata = OneTimeDatas.objects.all().first()
        print(btnID)
        data = Auto_save_Data.objects.get(ScrimUniqueId = f'{btnID}')
        datas = {'scrimData':f'{data}'}
        print(datas)
        print(data.ScrimDate)

        
    return render(request,'addperfdata.html',{"scrimData":data,"plyData":pdata,"uid":btnID})

def matchData(request):
    full_data = {}
    from Registration_soft.utils.performance_page import Performance_manage_in
    KP = 0
    plp = 0
    for i in range(1,7):
        # print(button_Stat)
        if request.method == "POST" :
            button_Stat = request.POST.get(f'userP{i}','off')
            user_P1 = request.POST.get(F'killsp{i}')
            print(button_Stat,user_P1,'yahi hia')

            name_kill = {f'userPlayer{i}': {'pname':f'{button_Stat}','pkill':f'{user_P1}'}}

            # Performance_manage_in(button_Stat,user_P1)
            ukdata = {f'{button_Stat}':f'{user_P1}'}
            full_data.update(name_kill)
            feedback = request.POST.get('feedback')
            position = request.POST.get('position')
            if user_P1 is not None :
                user_P1=int(user_P1)
                KP = user_P1 +KP
                print(type(user_P1))
            uid = request.POST.get('uid')
            unique_id = {'uid':f'{uid}'}
    print(name_kill)
    print(full_data)
    print(feedback,position,KP,uid)
    addnote = {'feedback':f'{feedback}'}
    killPoint = {'killPoint':f'{KP}'}
    position = int(position)
    for i in range(2,8):
        if position ==1:
            plpoint ={'pp': '10'}
            pp = 10
        elif position ==i and i<8:
            pp = 6-plp
            plpoint ={'pp': f'{pp}'}
        elif position ==8:
            plpoint ={'pp':'1'}
            pp = 1
        plp = plp +1

    TP = KP + pp
    TotlPoint = {'TP':f'{TP}'}
    full_data.update(addnote)
    full_data.update(killPoint)
    full_data.update(TotlPoint)
    full_data.update(plpoint)
    full_data.update(unique_id)

    for no in range(1,7):
        if full_data[f'userPlayer{no}']['pname'] == 'off':
            full_data.pop(f'userPlayer{no}')
    print('the full data is',full_data)
    Performance_manage_in(full_data)
    return HttpResponse('hlepp')

#scrim_name,scrim_time,scrim_kill,scrim_place,scrim_date,scrim_reason,scrim_topo 










