import ast
import time
import requests
from datetime import datetime
import threading
from django.http import HttpResponse
from django.shortcuts import render
i =0
def loginPage(request):
    flag = True
    return render(request,'login_signup.html')
def SignUpPage(request):
    return render(request,'SignUp.html')
def SignUp(request):
    from Registration_soft.utils.signUP_Login import SignUp
    uname =request.POST.get('USERNAME')
    upass =request.POST.get('PASSWORD')
    userExist = SignUp(uname,upass)
    return render(request,'SignUp.html',{"userExist":userExist,"time":datetime.now()})
            
def login(request):
    alert = False    
    if request.method == 'POST':
        from django.contrib.auth.hashers import check_password
        from django.contrib.auth.hashers import make_password
        from Registration_soft.models import userLogin
        uname =request.POST.get('USERNAME')
        upass =request.POST.get('PASSWORD')
        passhash = make_password(f'{upass}')
        uid= f'{uname}{upass}'
        try:
            userLogData = userLogin.objects.get(username = f'{uname}')
            passMatch = check_password(upass,userLogData.userpass)
            request.session['uid'] = uid
            if passMatch is True:
                from Registration_soft.models import PerfData
                data = PerfData.objects.filter(UserUniqueId = uid).first()
                return render(request,'index.html',{"perfdata":data,"uid":uid})
        except Exception as e:
            print(e)
            flag = True
            return render(request,'login_signup.html',{"alerts":flag,"time":datetime.now()})
            
        
def index(request):
    from Registration_soft.models import PerfData
    uid = request.session.get('uid')
    try:
        data = PerfData.objects.filter(UserUniqueId = f'{uid}')
        print(uid)
    except Exception as e:
        data = e
    return render(request,'index.html',{"perfdata":data})
def registration(request):

    uid = request.session.get('uid')
    from Registration_soft.models import ScrimsData
    try:
        scrim_data = ScrimsData.objects.filter(UserUniqueId = uid)
    except Exception as e:
        scrim_data = e
    return render(request,'registration_ui.html',{"scrim_data": scrim_data})


def registration_Starter(request):
    from Registration_soft.utils.time_check import time_check
    from Registration_soft.models import ScrimsData
    uid = request.session.get('uid')
    print('infun')
    scrims = {}
    try:
        scrims_data = ScrimsData.objects.filter(UserUniqueId = uid)

        for data in scrims_data:
            button_Stat = request.POST.get(f'{data.ScrimsUid}','off')
            print(data.ScrimsId,button_Stat)

            if button_Stat == 'on':

                print('init')
                # thread = threading.Thread(target=time_check,args=(data.ScrimsRegTime,data.ScrimsId))
                thread = threading.Thread(target=time_check,args=(data,uid))
                thread.start()
                scrims.update({ f'{data.ScrimsName}': f'{data.ScrimsTime}'})

                from Registration_soft.utils.Scrims_Data_auto import auto_data

                auto_data(data.ScrimsName,data.ScrimsId,data.ScrimsTime,uid)
                print(scrims.keys(),'this is the key')
    except Exception as e:
        scrims = e
    return render(request,'registering.html',{"scrims":scrims})

    
            
def update_Data(request):
     return render(request,'Scrim_Data.html')


def AddData(request):
    from Registration_soft.utils.UpdateData import AddNewData
    uid = request.session.get('uid')
    AddNewData(request,uid)
    return render(request, 'Scrim_Data.html')

def AuthCheck(request):
    from Registration_soft.utils.UpdateData import OneTimeData
    uid = request.session.get('uid')
    OneTimeData(request,uid)
    return render(request,'auth_noti.html')

def PerfManage(request):
    from Registration_soft.models import Auto_save_Data
    uid = request.session.get('uid')
    try:
        data = Auto_save_Data.objects.filter(UserUniqueId = uid)
    except Exception as e:
        data = e
    return render(request, 'performance.html',{"PerfData":data})


def perfIN(request):
    uid = request.session.get('uid')
    if request.method == 'POST':
        btnID = request.POST.get('action')
        from Registration_soft.models import Auto_save_Data
        from Registration_soft.models import OneTimeDatas
        try:
            plData = OneTimeDatas.objects.get(UserUniqueId = uid)
            scData = Auto_save_Data.objects.filter(UserUniqueId = uid).get(ScrimUniqueId = f'{btnID}')
            print(scData,plData)
        except Exception as e:
            scData = e
    return render(request,'addperfdata.html',{"scrimData":scData,"plyData":plData,"uid":btnID})



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
            positioninmatch = {'position':position}
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
    full_data.update(positioninmatch)
    full_data.update(addnote)
    full_data.update(killPoint)
    full_data.update(TotlPoint)
    full_data.update(plpoint)
    full_data.update(unique_id)
    uuid = request.session.get('uid')
    for no in range(1,7):
        if full_data[f'userPlayer{no}']['pname'] == 'off':
            full_data.pop(f'userPlayer{no}')
    print('the full data is',full_data)
    Performance_manage_in(full_data,uuid)
    return HttpResponse('hlepp',uuid)


def manage_Data(request):
    return render(request,'editdata.html')
    

def manipulateData(request):
    if request.method == "POST":
        TaskPerfE = request.POST.get("PerformanceEdit")
        TaskPerfD = request.POST.get("PerformaceDel")
        TaskScrimsE = request.POST.get("ScrimsEdit")
        TaskScrimsD = request.POST.get("ScrimsDel")
        TaskOneTimeE = request.POST.get("OneTimeEdit")
        TaskOneTimeD = request.POST.get("OneTimeDel")
        useruid = request.session.get('uid')
        try:
            if TaskPerfE =='on':
                from Registration_soft.models import PerfData
                dataPerf = PerfData.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/PerfDataEdit.html',{"code":'E',"DEdata":dataPerf})
            if TaskPerfD =='on':
                from Registration_soft.models import PerfData
                dataPerf = PerfData.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/PerfDataDel.html',{"code":'D',"DEdata":dataPerf})
            if TaskScrimsE =='on':
                from Registration_soft.models import ScrimsData
                dataScrim = ScrimsData.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/ScrimsData.html',{"code":'E',"DEdata":dataScrim})
            if TaskScrimsD =='on':
                from Registration_soft.models import ScrimsData
                dataScrim = ScrimsData.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/ScrimsDataDel.html',{"code":'D',"DEdata":dataScrim})
            if TaskOneTimeE =='on':
                from Registration_soft.models import OneTimeDatas
                dataOneData = OneTimeDatas.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/manage_old_data.html',{"code":'E',"DEdata":dataOneData})
            if TaskOneTimeD =='on':
                from Registration_soft.models import OneTimeDatas
                dataOneData = OneTimeDatas.objects.filter(UserUniqueId = useruid)
                return render(request,'manageData/manage_old_data.html',{"code":'D',"DEdata":dataOneData})
        except Exception as e:
            return HttpResponse(f'the error is {e}')
  


def deData(request):
    try:
        if request.method =='POST':
            scrimId = request.POST.get('DEE')
            uid = request.session.get('uid')
            from Registration_soft.utils.datamanage import perfdata
            dataUid = perfdata(scrimId,uid)
            return render(request,'manageData/datamanage/PerfDatamanipulate.html',{"datascid":dataUid})
    except Exception as e:
        return HttpResponse(f'the error is {e}')
def delData(request):
    try:
        if request.method == 'POST':
            scrimId = request.POST.get('DEL')
            from Registration_soft.utils.datamanage import delData
            uid = request.session.get('uid')
            delData(scrimId,uid)
            from Registration_soft.models import PerfData
            uid = request.session.get('uid')
            dataPerf= PerfData.objects.filter(UserUniqueId = uid).all()
            return render(request,'manageData/PerfDataDel.html',{"code":'D',"DEdata":dataPerf})
    except Exception as e:
        return HttpResponse(f'the error is {e}')
def deScrimsData(request):
    try:
        if request.method == 'POST':
            scrimId = request.POST.get('SDE')
            from Registration_soft.utils.datamanage import scrimsData
            uid = request.session.get('uid')
            dataScrims = scrimsData(scrimId,uid)
            return render(request,'manageData/datamanage/ScrimsDatamanipulate.html',{"scrimsData":dataScrims})
    except Exception as e:
        return HttpResponse(f'the error is {e}')
def delScrimsData(request):
    try:
        if request.method == 'POST':
            scrimId = request.POST.get('SDEL')
        from Registration_soft.utils.datamanage import delScrimData
        uid = request.session.get('uid')
        delScrimData(scrimId,uid)
        from Registration_soft.models import ScrimsData
        dataScrim = ScrimsData.objects.all()
        return render(request,'manageData/ScrimsDataDel.html',{"DEdata":dataScrim})
    except Exception as e:
        return HttpResponse(f'the error is {e}')