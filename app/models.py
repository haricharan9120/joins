from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return str(self.dept_no)

class Emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=150)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    hire_date=models.DateField()
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.grade)

