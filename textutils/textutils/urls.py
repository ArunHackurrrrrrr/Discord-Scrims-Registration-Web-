"""
URL configuration for textutils project.

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
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('analyze',views.analyze,name='analyze'),
]



# notes dekho path ke baad ka pahla string vo url ka end point /word hota hai for eg.http://127.0.0.1:8000/boobs here boobs is end point and second string vo fuction hota hai jisko run hona chahiye is url par and last me jo name ka matlab ye hai ki is path ka naam rakh diya hai and now we can acces it from anywhere in this project using tempelataes

