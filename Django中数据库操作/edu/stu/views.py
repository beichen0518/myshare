from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def addstu(request):
    if request.method == 'GET':
        return render(request, 'stu_enter.html')
    if request.method == 'POST':
        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        c_id = request.POST.get('c_id')
        stu_tel = request.POST.get('tel')
    Student.objects.create(
        stu_name=stu_name,
        stu_sex=stu_sex,
        stu_tel=stu_tel,
        c_id=c_id
    )
    return HttpResponse('提交学生信息成功')


def showStudent(request):
    p_cid = request.GET.get('p')
    c_id = int(p_cid)
    stus = Student.objects.filter(c_id=c_id)
    #不包含这个数据的所有信息
    # stus = Student.objects.exclude(c_id=c_id)
    return render(request, 'show_student.html', {'students' : stus})


