from django.db import models

# Create your models here.

class Dept(models.Model):
    departno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=40)
    loc=models.CharField(max_length=40)
    def __int__(self):
        return self.departno
    
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    departno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __int__(self) :
        return self.departno