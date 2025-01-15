from Registration_soft.models import PerfData
from django.http import HttpResponse
from django.shortcuts import render
def Performance_manage_in(data):
    # from Registration_soft.models import OneTimeDatas
    from Registration_soft.models import Auto_save_Data
    # plname = OneTimeDatas.objects.all().first()
    date = Auto_save_Data.objects.get(ScrimUniqueId = data['uid'])

    print(data.keys())
    d = data.keys()
    TP = 0
    # pldata = 

    Perfomance_data = PerfData(
        ScrimName = date.ScrimName,
        ScrimDate = date.ScrimDate,
        ScrimPosition = data['position'],
        killplayer1 = data['userPlayer1']['pkill'],
        killplayer2 = data['userPlayer2']['pkill'],
        killplayer3 = data['userPlayer3']['pkill'],
        killplayer4 = data['userPlayer4']['pkill'],
        Scrimplacementpoint = data['pp'],
        Scrimkillpoint = data['killPoint'],
        ScrimTotalPoint = data['TP'],
        ScrimReason = data['feedback'],
        ScrimUniqueId = data['uid'],
        PlayerName1 = data['userPlayer1']['pname'],
        PlayerName2 = data['userPlayer2']['pname'],
        PlayerName3 = data['userPlayer3']['pname'],
        PlayerName4 = data['userPlayer4']['pname'],
    )
    Perfomance_data.save()
    
    Auto_save_Data.objects.filter(ScrimUniqueId = data['uid']).delete()




def Performance_manage_show():
    from Registration_soft.models import PerfData

    data = PerfData.objects.all()
    nod = 0
    show_data = []
    for datas in data :
        if nod>2:
            return show_data
        else:
            partial_data = {f'data{nod}':{'scrimdate':f'{datas.ScrimDate}','scrimTP':f'{datas.ScrimTotalPoint}'}}
            show_data.append(partial_data)

        print(datas.ScrimUniqueId)
        