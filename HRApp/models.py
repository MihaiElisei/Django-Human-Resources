from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField
import datetime


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


# DEPARTMENT MODEL
class Department(models.Model):
    '''
     Department Employee belongs to. eg. Transport, Engineering.
    '''
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name', 'created']
    
    def __str__(self):
        return self.name


# ROLE MODEL
class Role(models.Model):
    '''
        Role Table eg. Staff,Manager,H.R ...
    '''
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125, null=True, blank=True)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name', 'created']

    def __str__(self):
        return self.name


# BANK DETAILS MODEL
class Bank(models.Model):
    employee = models.OneToOneField('Employee', help_text='select employee(s) to add bank account', on_delete=models.CASCADE, blank=False, primary_key=True)
    name = models.CharField(_('Name of Bank'), max_length=125, blank=False, null=True)
    account = models.CharField(_('Account Number'), help_text='employee account number', max_length=30, blank=False, null=True)
    branch = models.CharField(_('Branch'), help_text='which branch was the account issue', max_length=125, blank=True, null=True)
    salary = models.DecimalField(_('Starting Salary'), help_text='This is the initial salary of employee', max_digits=16, decimal_places=2, null=True, blank=False)

    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True, null=True)

    class Meta:
        verbose_name = _('Bank')
        verbose_name_plural = _('Banks')
        ordering = ['-name', '-account']

    def __str__(self):
        return ('{0}'.format(self.name))


# RELATIONSHIP MODEL
class Relationship(models.Model):
    MARRIED = 'Married'
    SINGLE = 'Single'
    DIVORCED = 'Divorced'
    WIDOW = 'Widow'
    WIDOWER = 'Widower'

    STATUS = (
    (MARRIED, 'Married'),
    (SINGLE, 'Single'),
    (DIVORCED, 'Divorced'),
    (WIDOW, 'Widow'),
    (WIDOWER, 'Widower'),
    )

    FATHER = 'Father'
    MOTHER = 'Mother'
    SIS = 'Sister'
    BRO = 'Brother'
    UNCLE = 'Uncle'
    AUNTY = 'Aunty'
    HUSBAND = 'Husband'
    WIFE = 'Wife'
    FIANCE = 'Fiance'
    FIANCEE = 'Fiancee'
    COUSIN = 'Cousin'
    NIECE = 'Niece'
    NEPHEW = 'Nephew'
    SON = 'Son'
    DAUGHTER = 'Daughter'

    NEXTOFKIN_RELATIONSHIP = (
    (FATHER, 'Father'),
    (MOTHER, 'Mother'),
    (SIS, 'Sister'),
    (BRO, 'Brother'),
    (UNCLE, 'Uncle'),
    (AUNTY, 'Aunty'),
    (HUSBAND, 'Husband'),
    (WIFE, 'Wife'),
    (FIANCE, 'Fiance'),
    (COUSIN, 'Cousin'),
    (FIANCEE, 'Fiancee'),
    (NIECE, 'Niece'),
    (NEPHEW, 'Nephew'),
    (SON, 'Son'),
    (DAUGHTER, 'Daughter'),
    )

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(_('Marital Status'), max_length=10, default=SINGLE, choices=STATUS, blank=False, null=True)
    spouse = models.CharField(_('Spouse (Fullname)'), max_length=255, blank=True, null=True)
    occupation = models.CharField(_('Occupation'), max_length=125, help_text='spouse occupation', blank=True, null=True)
    tel = PhoneNumberField(default=None, null = True, blank=True, verbose_name='Spouse Phone Number (Example +353240000000)', help_text= 'Enter number with Country Code Eg. +353240000000')
    children = models.PositiveIntegerField(_('Number of Children'), null=True, blank=True, default=0)

    nextofkin = models.CharField(_('Next of Kin'),max_length=255,blank=False,null=True,help_text='fullname of next of kin')
    contact = PhoneNumberField(verbose_name='Next of Kin Phone Number (Example +353240000000)',null=True,blank=True,help_text='Phone Number of Next of Kin')
    relationship = models.CharField(_('Relationship with Next of Person'),help_text='Who is this person to you ?',max_length=15,choices=NEXTOFKIN_RELATIONSHIP,blank=False,null=True)

    father = models.CharField(_('Father\'s Name'),max_length=255,blank=True,null=True)
    foccupation = models.CharField(_('Father\'s Occupation'),max_length=125,help_text='',blank=True,null=True)

    mother = models.CharField(_('Mother\'s Name'),max_length=255,blank=True,null=True)
    moccupation = models.CharField(_('Mother\'s Occupation'),max_length=125,help_text='',blank=True,null=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)

    class Meta:
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'
        ordering = ['created']


    def __str__(self):
        if self.status == 'Married':
            return self.spouse
        return self.status


# EMERGENCY MODEL
class Emergency(models.Model):
    FATHER = 'Father'
    MOTHER = 'Mother'
    SIS = 'Sister'
    BRO = 'Brother'
    UNCLE = 'Uncle'
    AUNTY = 'Aunty'
    HUSBAND = 'Husband'
    WIFE = 'Wife'
    FIANCE = 'Fiance'
    FIANCEE = 'Fiancee'
    COUSIN = 'Cousin'
    NIECE = 'Niece'
    NEPHEW = 'Nephew'
    SON = 'Son'
    DAUGHTER = 'Daughter'

    EMERGENCY_RELATIONSHIP = (
    (FATHER,'Father'),
    (MOTHER,'Mother'),
    (SIS,'Sister'),
    (BRO,'Brother'),
    (UNCLE,'Uncle'),
    (AUNTY,'Aunty'),
    (HUSBAND,'Husband'),
    (WIFE,'Wife'),
    (FIANCE,'Fiance'),
    (COUSIN,'Cousin'),
    (FIANCEE,'Fiancee'),
    (NIECE,'Niece'),
    (NEPHEW,'Nephew'),
    (SON,'Son'),
    (DAUGHTER,'Daughter'),
    )

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(_('Fullname'),help_text='who should we contact ?', max_length=255, null=True ,blank=False)
    tel = PhoneNumberField(default='+353240000000', null = False, blank=False, verbose_name='Phone Number (Example +353240000000)', help_text= 'Enter number with Country Code Eg. +353240000000')
    location = models.CharField(_('Place of Residence'),max_length= 125,null=True,blank=False)
    relationship = models.CharField(_('Relationship with Person'),help_text='Who is this person to you ?',max_length=8,default=FATHER,choices=EMERGENCY_RELATIONSHIP,blank=False,null=True)


    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)

    class Meta:
        verbose_name = 'Emergency'
        verbose_name_plural = 'Emergency'
        ordering = ['-created']


    def __str__(self):
        return self.fullname


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
    id = models.CharField(_('Employee ID Number'), max_length=10, null=False, blank=False, primary_key=True)
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
    is_blocked = models.BooleanField(_('Is Blocked'),help_text='button to toggle employee block and unblock',default=False)
    is_deleted = models.BooleanField(_('Is Deleted'),help_text='button to toggle employee deleted and undelete',default=False)

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


