def auto_data(Scrim_Name,Scrim_Id,Scrim_Time,useruid):
    from Registration_soft.models import Auto_save_Data
    from datetime import date
    from datetime import datetime
    Scrim_Date = date.today()
    registration_time = datetime.now().time()
    uniqueId = f'{Scrim_Date}{registration_time}'
    AutoSaveData = Auto_save_Data(

        ScrimName = Scrim_Name,
        ScrimId = Scrim_Id,
        ScrimDate = Scrim_Date,
        ScrimTime = Scrim_Time,
        ScrimUniqueId = uniqueId,
        UserUniqueId = useruid
    
    )

    print(uniqueId,useruid,'uid from scrimdataauto')


    AutoSaveData.save()

