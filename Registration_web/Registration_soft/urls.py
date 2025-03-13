"""
URL configuration for Registration_soft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:   
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Registration_soft import views

urlpatterns = [
    path('home', views.index, name= 'index'),
    path('registration',views.registration, name='reigister'),
    path('Register_scrim',views.registration_Starter, name='Register_scrim'),
    path('UpdateData',views.update_Data, name='UpdateData'),
    path('add-data/', views.AddData, name='UpdateData'),
    path('AuthCheck', views.AuthCheck, name='AddDatas'),
    path('perfmanage', views.PerfManage, name='PerfManage'),
    path('AddData', views.perfIN, name='AddData'),
    path('addmatchdata',views.matchData),
    path('managedata',views.manage_Data),
    path('delOReditData',views.manipulateData),
    path('DEDATA',views.deData),
    path('DELDATA',views.delData),
    path('SCDATAEDIT',views.deScrimsData),
    path('SCDATADEL',views.delScrimsData),
    path('',views.loginPage),
    path('login', views.login),
    path('SignUpPage', views.SignUpPage),
    path('SignUp',views.SignUp)

]
