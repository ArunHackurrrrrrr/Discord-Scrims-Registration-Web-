def auto_data(Scrim_Name,Scrim_Id,Scrim_Time):
    from Registration_soft.models import Auto_save_Data
    from datetime import date
    Scrim_Date = date.today()
    AutoSaveData = Auto_save_Data(

        ScrimName = Scrim_Name,
        ScrimId = Scrim_Id,
        ScrimDate = Scrim_Date,
        ScrimTime = Scrim_Time
    )

    print(Scrim_Date,Scrim_Id,Scrim_Name,Scrim_Time)


    AutoSaveData.save()

def DataUp():
    from Registration_soft.models import Auto_save_Data
    data = Auto_save_Data.objects.all()