from multiprocessing.dummy import JoinableQueue
from django.contrib import admin
from jobboard.models import Employee,Joboffer

admin.site.register(Employee)
admin.site.register(Joboffer)


