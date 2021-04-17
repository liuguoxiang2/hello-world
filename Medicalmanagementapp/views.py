
from django.shortcuts import render, redirect
from django.shortcuts import render

from Medicalmanagement.pands import getCount_Dict
from Medicalmanagement.utils.read_file import file_upload
from Medicalmanagementapp.models import medicalRecord




def fileupload(request):
    if request.method == 'POST':# 获取对象
        obj = request.FILES.get('fafafa')
        k1 = file_upload(obj)
        querysetlist = []
        for information  in k1:
            querysetlist.append(medicalRecord(name=information[0], sex=information[1], date=information[5], syndrome=information[2], source=information[4],
                                         combination=information[3]))
        medicalRecord.objects.bulk_create(querysetlist)
        return redirect("/show/")

    if request.method=='GET':
        return render(request, 'fileupload.html')


def upload(request):
    if request.method=='GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
        name=request.POST.get('name');
        sex=request.POST.get('sex');
        date=request.POST.get('date');
        syndrome=request.POST.get('syndrome');
        source=request.POST.get('source');
        combination=request.POST.get('combination');
        medicalRecord.objects.create(name=name,sex=sex,date=date,syndrome=syndrome,source=source,combination=combination)
        all_info = medicalRecord.objects.all();
        return  render(request, 'show.html',{'msg':all_info})


def index(request):
    return render(request, 'index.html')


def show(request):
    all_info = medicalRecord.objects.all();
    return render(request, 'show.html',{'msg':all_info})

def delete(request):
    did=request.GET.get('did');
    print( medicalRecord.objects.get(id=did));
    medicalRecord.objects.get(id=did).delete();
    return redirect("/modify/")

def modify(request):
    if request.method == 'GET':
     all_info = medicalRecord.objects.all();
     return render(request, 'modify.html', {'msg': all_info})
    if request.method == 'POST':
        id=request.POST.get('id');
        name = request.POST.get('name');
        sex = request.POST.get('sex');
        date1 = request.POST.get('date').replace(r'年', '-').replace(r'月', '-').replace(r'日', '')
        print(date1)
        syndrome = request.POST.get('syndrome');
        source = request.POST.get('source');
        combination = request.POST.get('combination');
        medicalRecord.objects.filter(id=id).update(name=name,sex=sex,date=date1,syndrome=syndrome,source=source,combination=combination)
        print(name)
        return redirect("/modify/")

def  Frequencyanalysis(request):
        return render(request, 'analysis/Frequencyanalysis.html')

def AnalysisResult(request):
    if request.method == 'POST':
        data_dict={}
        obj = request.FILES.get('fafafa')
        k1=getCount_Dict(data_dict,obj)
        return render(request, 'analysis/AnalysisResult.html',{'msg':k1})


    if request.method=='GET':
      return render(request, 'analysis/AnalysisResult.html')