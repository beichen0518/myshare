from django.db import models

# Create your models here.


class EduClass(models.Model):
    c_name = models.CharField(max_length=5)
    c_desc = models.CharField(max_length=15)

    class Meta:
        db_table = 'tbclass'

