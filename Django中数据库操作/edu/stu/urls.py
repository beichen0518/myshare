from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'^addstu/', views.addstu),
    url(r'^showstu', views.showStudent)
]