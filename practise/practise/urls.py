"""
URL configuration for practise project.

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
from task.views import datas,stores,instagram,travel,deldata,update_datas
from Nuhachillcare.views import delete_data,update_data,service,getservicecharge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',datas, name="home"),
    path('first/',stores,name="first"),
    path('second/',instagram,name="second"),
    path('third/',travel,name="third"),
    path('updates/<int:id>/',update_datas,name="updatedatas"),
    path('del/<int:id>/',deldata,name="deldata"),
    # paths for nuhachillcare app

    path('index/',service,name='index'),
    path('delete/<int:id>/',delete_data,name="deletedata"),
    path('update/<int:id>/',update_data,name="updatedata"),
    path('getserviceamount/',getservicecharge,name="getservicecharge"),

    
]
