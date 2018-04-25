from django.conf.urls import url

from e_class import views

urlpatterns = [
    url(r'^addcls/', views.addcls),
    url(r'^showcls/',views.showClass )
]