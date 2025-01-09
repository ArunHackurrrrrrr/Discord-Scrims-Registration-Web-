from Registration_soft.models import PerfData

def Performance_manage_in(data):
    from Registration_soft.models import OneTimeDatas
    plname = OneTimeDatas.objects.all().first()
    print(data.keys())
    d = data.keys()
    TP = 0
    # pldata = 

    Perfomance_data = PerfData(
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
        PlayerName4 = data['userPlayer4']['pname']
    )
    Perfomance_data.save()
    from Registration_soft.models import Auto_save_Data
    Auto_save_Data.objects.filter(ScrimUniqueId = data['uid']).delete()




def Performance_manage_show():
    from Registration_soft.models import Auto_save_Data

    data = Auto_save_Data.objects.all()

    for datas in data :
        print(datas.ScrimDate)
        # return datas