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


