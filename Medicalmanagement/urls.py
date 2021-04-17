"""Medicalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import path
from django.conf.urls import url

from django_extensions.settings import BASE_DIR

from Medicalmanagementapp import views
from Medicalmanagement.pands import getCount_Dict


# def login(request):
#     inpath = 'G:\毕业论文\中风病大全整理.xlsx'  # excel文件所在路径
#     data_dict = {}
#     k1=getCount_Dict(data_dict,inpath)
#     print(k1)
#     return  render(request,'show.html',{'msg':k1})




# 匹配字符串，对应处理函数，
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('delete/', views.delete, name="delete"),
    path('show/', views.show, name="show"),
    path('fileupload/',views.fileupload,name="fileupload"),
    path('index/',views.index,name="index"),
    path('upload/', views.upload, name="upload"),
    path('modify/', views.modify, name="modify"),
    path('Frequencyanalysis/', views.Frequencyanalysis, name="Frequencyanalysis"),
    path('AnalysisResult/', views.AnalysisResult, name="AnalysisResult"),
    url(r'^$', views.index),

]
