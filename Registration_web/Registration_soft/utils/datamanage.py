def perfdata(uid,userid):
    from Registration_soft.models import PerfData
    data = PerfData.objects.filter(UserUniqueId = userid).get(ScrimUniqueId = uid)
    return data

def delData(uid,userid):
    from Registration_soft.models import PerfData
    PerfData.objects.filter(UserUniqueId = userid).get(ScrimUniqueId = uid).delete()

def scrimsData(uid,userid):
    from Registration_soft.models import ScrimsData
    data = ScrimsData.objects.filter(UserUniqueId = userid).get(ScrimsId = uid)
    return data
def delScrimData(uid,userid):
    from Registration_soft.models import ScrimsData
    ScrimsData.objects.filter(UserUniqueId = userid).get(ScrimsId = uid).delete()
    