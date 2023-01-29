from django.db import models
import datetime


class EmployeeManager(models.Manager):
    def birthdays_current_month(self):
        '''
        This Method Fetches all the active users,whose date of birthday is in current month, "this month".
        Every month list all employees whose birthday is in that month.
        '''
        current_date = datetime.date.today()
        return super().get_queryset().filter(is_blocked = False).filter(birthday__month = current_date.month)


class LeaveManager(models.Manager):
	def get_queryset(self):
		'''
		overrides objects.all() 
		return all leaves including pending or approved
		'''
		return super().get_queryset()



	def all_pending_leaves(self):
		return super().get_queryset().filter(status = 'pending').order_by('-created')




	