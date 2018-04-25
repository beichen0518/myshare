from django.conf.urls import url

from management import views

urlpatterns = [
    url(r'^adduser/', views.addUser),
    url(r'^search/', views.showPer),
    url(r'^isper/', views.isPer)
]