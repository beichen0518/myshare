from django.db import models

# Create your models here.


class Role(models.Model):
    r_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tbrole'


class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_sex = models.BooleanField()
    u_birth = models.DateField()
    u_operate_time = models.DateTimeField(auto_now=True)
    u_create_time = models.DateTimeField(auto_now_add=True)
    r = models.ForeignKey(Role, null=True)

    class Meta:
        db_table = 'tbuser'


class Permission(models.Model):
    p_name = models.CharField(max_length=20)
    p_role = models.ManyToManyField(Role)

    class Meta:
        db_table = 'tbpermission'
