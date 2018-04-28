from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def createUser(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        upassword = request.POST.get('password')
    user = User.objects.create_user(
        username=username,
        password=upassword
    )
    user.is_staff = True
    user.save()
    return HttpResponse('创建成功')


def myIndex(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/uauth/accounts/login/')
