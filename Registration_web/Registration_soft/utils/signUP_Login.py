def SignUp(name,password):
    from django.contrib.auth.hashers import make_password
    from Registration_soft.models import userLogin
    hashPass = make_password(f'{password}')
    userExist = False
    userUID = f'{name}{hashPass}'
    for data in userLogin.objects.all():
        if data.username == name:
            userExist = True
    if userExist != True:
        make_New_User = userLogin(
            username = name,
            userpass = hashPass,
            userUniqueId = userUID
        )
        make_New_User.save()
        return 'created'
    else:
        return True
    
