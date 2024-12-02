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
    ScrimName = models.CharField(max_length=20)
    ScrimTime = models.TimeField()
    Scrimkill = models.PositiveIntegerField()
    Scrimplacement = models.IntegerField()
    ScrimDate = models.DateField()
    ScrimReason = models.CharField(max_length=200)
    ScrimTotalPoint = models.IntegerField()
    def __str__(self):
        return f"{self.ScrimDate} - {self.ScrimTotalPoint}"     
    

class OneTimeDatas(models.Model):
    UserAuth = models.CharField(max_length=200)
    UserName = models.CharField(max_length=20)
    UserTeam = models.CharField(max_length=20)
    UserDcId = models.CharField(max_length=200)
    UserPlayer1 = models.CharField(max_length=50)
    UserPlayer2 = models.CharField(max_length=50)
    UserPlayer3 = models.CharField(max_length=50)
    UserPlayer4 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.UserName} - {self.UserTeam}"

class Auto_save_Data(models.Model):
    ScrimName = models.CharField(max_length=20)
    ScrimId = models.CharField(max_length=200)
    ScrimDate = models.DateField()
    ScrimTime = models.TimeField()
