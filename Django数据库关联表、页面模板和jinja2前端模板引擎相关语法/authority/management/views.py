from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from management.models import User


def addUser(request):
    if request.method == 'GET':
        return render(request, 'adduser.html')
    if request.method == 'POST':
        u_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            u_sex = 1
        else:
            u_sex = 0
    u_birth = request.POST.get('birth')
    r_id = int(request.POST.get('rid'))

    User.objects.create(
        u_name=u_name,
        u_sex=u_sex,
        u_birth=u_birth,
        r_id=r_id
    )
    return render(request, 'adduser.html')


def showPer(request):
    if request.method == 'GET':
        return render(request, 'search_per.html')
    if request.method == 'POST':
        u_name = request.POST.get('name')
    user = User.objects.get(u_name=u_name)
    pers = user.r.permission_set.all()
    return render(request, 'showper.html', {'user': user, 'pers' : pers})


def isPer(request):
    if request.method == 'GET':
        return render(request, 'isper.html')
    if request.method == 'POST':
        u_name = request.POST.get('name')
        p_name = request.POST.get('per')
    user = User.objects.get(u_name=u_name)
    if user.r.permission_set.filter(p_name=p_name):
        return HttpResponse('%s 有 %s' %(u_name, p_name))
    else:
        return HttpResponse('%s 没有 %s' %(u_name, p_name))
