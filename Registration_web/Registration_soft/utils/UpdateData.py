def AddNewData(request):
    if request.method == "POST":
        discord_id = request.POST.get('discord_id')
        scrim_name = request.POST.get('scrim_name')
        org_name = request.POST.get('org_name')
        registration_time = request.POST.get('registration_time')
        start_time = request.POST.get('start_time')
        start_date = request.POST.get('scrim_date')
        
        from Registration_soft.models import ScrimsData

        ScrimDAtaUser = ScrimsData(
            ScrimsName = scrim_name,
            ScrimsTime = start_time,
            ScrimsRegTime = registration_time,
            ScrimsId = discord_id,
            ScrimsOrg = org_name,
            ScrimsDate = start_date
        )
        ScrimDAtaUser.save()


def OneTimeData(request):
    if request.method == "POST":
        user_id = request.POST.get('discord_id')
        user_name = request.POST.get('User_Name')
        user_Team = request.POST.get('Team_name')
        user_Auth = request.POST.get('AuthID')
        user_P1 = request.POST.get('Player1')
        user_P2 = request.POST.get('Player2')
        user_P3 = request.POST.get('Player3')
        user_P4 = request.POST.get('Player4')

        from Registration_soft.models import OneTimeDatas

        UserData = OneTimeDatas(
            UserAuth = user_Auth,
            UserName = user_name,
            UserTeam = user_Team,
            UserDcId = user_id,
            UserPlayer1= user_P1,
            UserPlayer2 = user_P2,
            UserPlayer3 = user_P3,
            UserPlayer4 = user_P4,
        )

        UserData.save()

def delete_data(request):
    pass
