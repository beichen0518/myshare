from django.conf.urls import url
from django.contrib.auth.views import login, logout

from uauth import views

urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^createuser/', views.createUser),
]