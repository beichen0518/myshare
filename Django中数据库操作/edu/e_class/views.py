from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from e_class.models import EduClass


def addcls(request):
    if request.method == 'GET':
        return render(request, 'cls_enter.html')
    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_desc = request.POST.get('desc')
    EduClass.objects.create(
        c_name=c_name,
        c_desc=c_desc
    )
    return HttpResponse('添加信息成功')


def showClass(request):
    cl = EduClass.objects.all()
    return render(request, 'show_class.html', {'class' : cl})
