from django.shortcuts import render
from app.models import *

# Create your views here.
def table(request):
    lot=Dept.objects.all()
    d={'name':lot}
    return render(request,'table.html',d)


def rollex(request):
    loe=Employee.objects.all()
    d={'naukri':loe}
    return render(request,'emp.html',d)