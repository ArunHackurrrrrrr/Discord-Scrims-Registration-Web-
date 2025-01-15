def perfdata(uid):
    from Registration_soft.models import PerfData
    data = PerfData.objects.get(ScrimUniqueId = uid)
    return data

def delData(uid):
    from Registration_soft.models import PerfData
    PerfData.objects.get(ScrimUniqueId = uid).delete()

def scrimsData(uid):
    from Registration_soft.models import ScrimsData
    data = ScrimsData.objects.get(ScrimsId = uid)
    return data
def delScrimData(uid):
    from Registration_soft.models import ScrimsData
    ScrimsData.objects.get(ScrimsId = uid).delete()