from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class Employee(models.Model):
    name = models.CharField(max_length=50)
    headquarter = CountryField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name



class Joboffer(models.Model):
    company_name = models.ForeignKey(Employee,
                                    on_delete=models.CASCADE,
                                    related_name='joboffers')
    company_email = Employee.email
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = MoneyField(decimal_places=0,default=0,default_currency='USD',max_digits=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.job_title} needed in {self.city},{self.state}'
                
