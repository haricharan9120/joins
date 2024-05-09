from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
from app.models import *


def insert_dept(request):
    dn=input('enter deptno')
    dna=input('enter dname')
    dl=input('enterb location')
    DO=Dept.objects.get_or_create(dept_no=dn,dname=dna,location=dl)[0]
    DO.save()
    d={'QLDO':Dept.objects.all()}
    return render(request,'display_dept.html',d)


def insert_emp(request):


    eno=input('enter empno')
    en=input('enter ename')
    j=input('enter job')
    dn=input('enter deptno')
    m=input('enter mgr')
    s=input('enter sal')
    h=input('enter hiredate')
    c=input('enter comm')
    LDO=Dept.objects.filter(dept_no=dn)
    if LDO:
        DO=LDO[0]
        EO=Emp.objects.get_or_create(emp_no=eno,ename=en,job=j,dept_no=dn,mgr=m,sal=s,hire_date=h,comm=c)[0]
        EO.save()
        d={'QLEO':Emp.objects.all()}
        return render(request,'display_emp.html',d)
    else:
        return HttpResponse('no such dept is available in parent table')
    


def insert_salgrade(request):
    
    


    g=input('enter grade')
    ls=input('enter losal')
    hs=input('hisal')
    SO=Salgrade.objects.get_or_create(grade=g,losal=ls,hisal=hs)[0]
    SO.save()
    d={'QLSO':Salgrade.objects.all()}

    return render(request,'display_salgrade.html',d)










def display_dept(request):
    QLDO=Dept.objects.all()

    d={'QLDO':QLDO}
    return render(request,'display_dept.html',context=d)



def display_emp(request):
    QLEO=Emp.objects.all()
    
    
    
    QLEO=Emp.objects.filter(ename__startswith='j', ename__endswith='s')
    QLEO=Emp.objects.filter(Q(ename__startswith='j') | Q(ename__endswith='n'))
    
    

    
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',context=d)



def display_salgrade(request):
    QLSO=Salgrade.objects.all()
    


    QLSO=Salgrade.objects.filter(losal__range=[200,1000])

    QLSO=Salgrade.objects.all()


    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',context=d)



def innerequijoins(request):
    JDED=Emp.objects.select_related('dept_no').all()
    JDED=Emp.objects.select_related('dept_no').filter(ename='SMITH')
    JDED=Emp.objects.select_related('dept_no').filter(job='SALESMAN')
    JDED=Emp.objects.select_related('dept_no').all()
    JDED=Emp.objects.select_related('dept_no').filter( job__contains='A')
    JDED=Emp.objects.select_related('dept_no').filter(dept_no='10' )
    JDED=Emp.objects.select_related('dept_no').filter(sal = '1250' )
    JDED=Emp.objects.select_related('dept_no').filter(comm='200' )
    JDED=Emp.objects.select_related('dept_no').filter(sal__range=[1500,3000] )
    JDED=Emp.objects.select_related('dept_no').filter(job__in=['SALESMAN','CLERK'] )
    JDED=Emp.objects.select_related('dept_no').filter(emp_no__in=['7369','7654'] )
    JDED=Emp.objects.select_related('dept_no').all()
    JDED=Emp.objects.select_related('dept_no').filter(comm=0.0 )
    JDED=Emp.objects.select_related('dept_no').filter(ename__startswith='k' )
    JDED=Emp.objects.select_related('dept_no').filter(job__endswith='n')
    JDED=Emp.objects.select_related('dept_no').filter(Q(sal__startswith='8') | Q(hire_date__year__endswith='1995') )
    JDED=Emp.objects.select_related('dept_no').filter(dept_no__dname='RESEARCH')
    JDED=Emp.objects.select_related('dept_no').filter(comm__isnull=True)
    








    d={'JDED':JDED}


    return render(request,'innerequijoins.html',d)

def selfjoins(request):
    EMJD=Emp.objects.select_related('mgr').all()
    EMJD=Emp.objects.select_related('mgr').filter(sal__gt=1000)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__sal__lt=1000)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__ename__contains='A')
    EMJD=Emp.objects.select_related('mgr').filter(mgr__sal__isnull=True)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__sal__isnull=False)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=True)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=False)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__dept_no=20)
    EMJD=Emp.objects.select_related('mgr').filter(dept_no=10)
    EMJD=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    EMJD=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    EMJD=Emp.objects.select_related('mgr').filter(job='SALESMAN')
    EMJD=Emp.objects.select_related('mgr').filter(job__endswith='K')
    EMJD=Emp.objects.select_related('mgr').filter(mgr__job='SALESMAN')
    EMJD=Emp.objects.select_related('mgr').filter(mgr__job__startswith='S')
    EMJD=Emp.objects.select_related('mgr').filter(comm__range=[10,10000])
    EMJD=Emp.objects.select_related('mgr').filter(sal__range=[1000,10000])


    d={'EMJD':EMJD}
    return render(request,'selfjoins.html',d)


def empmgrdept(request):
    EMDJD=Emp.objects.select_related('dept_no','mgr').all()
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(ename__contains='k')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(job='SALESMAN')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(comm__isnull=True)
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(sal__range=[1000,3000])
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(mgr__ename='SMITH')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(dept_no__location='CHICAGO')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(dept_no__dname='RESEARCH')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(mgr__ename__contains='k')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(mgr__sal__range=[10,2000])
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(ename__startswith='A')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(job__endswith='r')
    EMDJD=Emp.objects.select_related('dept_no','mgr').filter(ename__startswith='J',dept_no__dname__endswith='G')

    d={'EMDJD':EMDJD}
    return render(request,'empmgrdept.html',d)