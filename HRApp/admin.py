from django.contrib import admin
from .models import Employee, Role, Department, Nationality, Bank, Relationship, Emergency

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Nationality)
admin.site.register(Bank)
admin.site.register(Relationship)
admin.site.register(Emergency)


