from django.db import models

# Create your models here.


class Student(models.Model):
    stu_name = models.CharField(max_length=5)
    stu_sex = models.BooleanField()
    stu_tel = models.CharField(max_length=11)
    c_id = models.IntegerField(max_length=3)
    stu_create_time = models.DateTimeField(auto_now_add=True)
    stu_change_time = models.DateTimeField(auto_now=True)
    is_existed = models.BooleanField(default=1)

    class Meta:
        db_table = 'tbstudent'

