from django.db import models

class ScrimsData(models.Model):
    ScrimsName = models.CharField(max_length=20)
    ScrimsTime = models.TimeField()
    ScrimsRegTime = models.TimeField()
    ScrimsId = models.IntegerField()
    ScrimsOrg = models.CharField(max_length=200)
    ScrimsDate = models.DateField()
    def __str__(self):
        return f"{self.ScrimsName} - {self.ScrimsTime}"     
class PerfData(models.Model):
    ScrimName = models.CharField(max_length=20,default='not models')
    ScrimPosition = models.CharField(max_length=10,default='#24')
    ScrimDate = models.CharField(max_length=20,default='not found')
    ScrimUniqueId = models.CharField(max_length=15,default='none')
    Scrimkillpoint = models.PositiveIntegerField()
    Scrimplacementpoint = models.IntegerField()
    ScrimReason = models.CharField(max_length=200,default='reason not given')
    ScrimTotalPoint = models.IntegerField()
    killplayer1 = models.CharField(max_length=10,default='not played')
    killplayer2 = models.CharField(max_length=10,default='not played')
    killplayer3 = models.CharField(max_length=10,default='not played')
    killplayer4 = models.CharField(max_length=10,default='not played')
    PlayerName1 = models.CharField(max_length=20,default='none')
    PlayerName2 = models.CharField(max_length=20,default='none')
    PlayerName3 = models.CharField(max_length=20,default='none')
    PlayerName4 = models.CharField(max_length=20,default='none')


    def __str__(self):
        return f"{self.Scrimkillpoint} - {self.ScrimTotalPoint}"     
    

class OneTimeDatas(models.Model):
    UserAuth = models.CharField(max_length=200)
    UserName = models.CharField(max_length=20)
    UserTeam = models.CharField(max_length=20)
    UserDcId = models.CharField(max_length=200)
    UserPlayer1 = models.CharField(max_length=50)
    UserPlayer2 = models.CharField(max_length=50)
    UserPlayer3 = models.CharField(max_length=50)
    UserPlayer4 = models.CharField(max_length=50)
    UserPlayer5 = models.CharField(max_length=50,default='none')
    UserPlayer6 = models.CharField(max_length=50,default='none')

    def __str__(self):
        return f"{self.UserName} - {self.UserTeam}"

class Auto_save_Data(models.Model):
    ScrimName = models.CharField(max_length=20)
    ScrimId = models.CharField(max_length=200)
    ScrimDate = models.DateField()
    ScrimTime = models.TimeField()
    ScrimUniqueId = models.CharField(max_length=50,default='uniqueID')

    def __str__(self):
        return f"{self.ScrimName} - {self.ScrimDate}"
