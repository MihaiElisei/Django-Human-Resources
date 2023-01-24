from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField


# NATIONALITY MODEL
class Nationality(models.Model):
    name = models.CharField(max_length=125)
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationality')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


# EMPLOYEE MODEL
class Employee(models.Model):
    # GENDER
    MALE = 'male'
    FEMALE = 'female'
    GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    )

    # TITLE
    MR = 'Mr'
    MRS = 'Mrs'
    MSS = 'Mss'
    DR = 'Dr'
    SIR = 'Sir'
    MADAM = 'Madam'
    TITLE = (
    (MR, 'Mr'),
    (MRS, 'Mrs'),
    (MSS, 'Mss'),
    (DR, 'Dr'),
    (SIR, 'Sir'),
    (MADAM, 'Madam'),
    )
    # EMPLOYMENT TYPE
    FULL_TIME = 'Full-Time'
    PART_TIME = 'Part-Time'
    CONTRACT = 'Contract'
    INTERN = 'Intern'
    EMPLOYEETYPE = (
    (FULL_TIME, 'Full-Time'),
    (PART_TIME, 'Part-Time'),
    (CONTRACT, 'Contract'),
    (INTERN, 'Intern'),
    )
    # EDUCATION
    MASTERS = 'Masters Degree'
    BACHELOR = 'Bachelor Degree'
    ADVANCED = 'Craft / Higher Certificate'
    LEAVING = 'Leaving Certificate'
    JUNIOR = 'Junior Certificate'
    OTHER = 'Other'
    EDUCATIONAL_LEVEL = (
    (MASTERS, 'Masters Degree'),
    (BACHELOR, 'Bachelor Degree'),
    (ADVANCED, 'Craft / Higher Certificate'),
    (LEAVING, 'Leaving Certificate'),
    (JUNIOR, 'Junior Certificate'),
    (OTHER, 'Other'),
    )

    # PERSONAL DATA
    id = models.CharField(_('Employee ID Number'), max_length=10, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(_('Title'), max_length=5, default=MR, choices=TITLE, blank=False, null=False)
    firstname = models.CharField(_('First Name'), max_length=125, null=False, blank=False)
    lastname = models.CharField(_('Last Name'), max_length=125, null=False, blank=False)
    othername = models.CharField(_('Other Name (optional)'), max_length=125, null=True, blank=True)
    sex = models.CharField(_('Gender'), max_length=9, choices=GENDER, blank=False)
    email = models.CharField(_('Email'), max_length=255, default=None, blank=False, null=False)
    tel = PhoneNumberField(default='+353000000000', null=False, blank=False, verbose_name='Phone Number (Example +353000000000)', help_text= 'Enter number with Country Code Eg. +353000000000')
    birthday = models.DateField(_('Birthday'), blank=False, null=False)
    nationality = models.ForeignKey(Nationality, verbose_name=_('Nationality'), on_delete=models.SET_NULL, null=True, default=None)
    address = models.CharField(_('Address'), help_text='address of current residence', max_length=125, null=True, blank=True)

    # EDUCATION & EXPERIENCE
    education = models.CharField(_('Education'),help_text='Highest educational level', max_length=26, choices=EDUCATIONAL_LEVEL, blank=False, null=True)
    lastwork = models.CharField(_('Last Place of Work'), help_text='Where was the last place you worked ?', max_length=125, null=True, blank=True)
    position = models.CharField(_('Position Held'),help_text='What position where you in your last place of work ?', max_length=255, null=True, blank=True)

    # COMPANY DATA
    department = models.ForeignKey(Department, verbose_name =_('Department'), on_delete=models.SET_NULL, null=True, default=None)
    role = models.ForeignKey(Role, verbose_name=_('Role'), on_delete=models.SET_NULL, null=True, default=None)
    startdate = models.DateField(_('Employement Date'), help_text='date of employement', blank=False, null=True)
    employeetype = models.CharField(_('Employee Type'), max_length=15, default=FULL_TIME, choices=EMPLOYEETYPE, blank=False, null=True)
    dateissued = models.DateField(_('Date Issued'), help_text='date staff id was issued', blank=False, null=True)
 
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True, null=True)
   
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        othername = self.othername

        if (firstname and lastname) or othername is None:
            fullname = firstname + ' ' + lastname
            return fullname
        elif othername:
            fullname = firstname + ' ' + lastname + ' ' + othername
            return fullname
        return

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return


