import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from app_company.models import *
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class Personnel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женшина')
    ]

    id_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    fathers_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Отчество')
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name='фото сотрудника')
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    email = models.EmailField(max_length=25, null=True, blank=True, verbose_name='e-mail')
    phone = models.IntegerField(null=True, blank=True, verbose_name='телефон')
    is_acceptance = models.BooleanField(default=True, verbose_name='Zatwierdzić')
    function = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='должность')
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, verbose_name='подразделение фирмы')

    def get_absolute_url(self):
        return reverse('personnel', kwargs={'slug': self.slug})



    # def get_absolute_url(self):
    #     return reverse('personnel-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'
        ordering = ['last_name']


class Employment(models.Model):
    CONTRACT_OF_EMPLOYMENT_A_FIXTED_TERM = 'CF'
    CONTRACT_OF_EMPLOYMENT_IDENFITE_PERIOD = 'CI'
    CONTRACT_AGREEMENT = 'CA'
    MANAGEMENT_CONTRACT = 'MC'
    CONTRACTS = [
        (CONTRACT_OF_EMPLOYMENT_A_FIXTED_TERM, 'Трудовой договор на неопределенный срок'),
        (CONTRACT_OF_EMPLOYMENT_IDENFITE_PERIOD, 'Срочный трудовой договор'),
        (CONTRACT_AGREEMENT, 'Договор подряда'),
        (MANAGEMENT_CONTRACT, 'Договор на оказание услуги')
    ]

    employee = models.ForeignKey(Personnel, on_delete=models.CASCADE, verbose_name='сотрудник')
    contract = models.CharField(max_length=2, choices=CONTRACTS, verbose_name='тип договора')
    employment_date_beginning = models.DateField(verbose_name='дата начала работы')
    employment_date_ending = models.DateField(verbose_name='дата окончания контракта')
    # contract_for_an_indefinite_period = models.BooleanField(employment_date_ending)
    salary = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Размер зар. п.')
    uploadedFile = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='скану документов', null=True, blank=True)
    uploadedFile_date = models.DateField(verbose_name='дата годности документа', null=True, blank=True)
    education_remarks = models.TextField(blank=True, null=True, verbose_name='замечания по образованию')
    deadline = models.DateField(blank=True, null=True, verbose_name=' срок устрониения')


    def __str__(self):
        return f"{self.employee}, {self.contract}, {self.employment_date_beginning}"

    class Meta:
        verbose_name = 'Трудоустройство'
        verbose_name_plural = 'Трудоустройство'
        ordering = ['id']


class PersonnelData(models.Model):
    employee = models.ForeignKey(Personnel, on_delete=models.CASCADE, verbose_name='сотрудник')
    born = models.DateField(verbose_name='День рождения')
    birth_place = models.CharField(max_length=50, verbose_name='Место рождения')
    birth_country = models.CharField(max_length=50, verbose_name='Страна рождения')
    '''living'''
    country = models.CharField(max_length=50, verbose_name='Страна постоянного проживания')
    city = models.CharField(max_length=50, verbose_name='Город постоянного проживания')
    post_code = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Почтовый индекс')
    street = models.CharField(max_length=100, verbose_name='Улица')
    street_number = models.CharField(max_length=10, verbose_name='Номер дома')
    house_number = models.CharField(max_length=10, verbose_name='Номер квартиры')
    '''education'''
    PRIMARY_EDUCATION = 'PE'
    SECONDARY_EDUCATION = 'SE'
    HIGHER_EDUCATION = 'HE'
    EDUCATION = [
        (PRIMARY_EDUCATION, 'Начальное образование'),
        (SECONDARY_EDUCATION, 'Среднее образование'),
        (HIGHER_EDUCATION, 'Высшее образование')
    ]
    education = models.CharField(max_length=2, choices=EDUCATION, verbose_name='образование')
    # qualifications = models.ManyToManyField(Qualifications, null=True, blank=True, verbose_name='Квалификации')
    uploadedFile = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='скану документов', null=True, blank=True)
    uploadedFile_date = models.DateField(verbose_name='дата годности документа')
    is_acceptance = models.BooleanField(default=True, verbose_name='Zatwierdzić')

    def __str__(self):
        return f"{self.employee}"

    class Meta:
        verbose_name = 'Личные данные'
        verbose_name_plural = 'Личные данные'
        # ordering = ['id']









# class Superiors(models.Model):
#     departament = models.ForeignKey(OrgStructure, on_delete=models.CASCADE, verbose_name='подразделение фирмы')
#     superior = models.ForeignKey(Personnel, on_delete=models.CASCADE,blank=True, null=True,  verbose_name='начальник')
#     level = models.IntegerField(validators=[MinValueValidator(0),
#                                             MaxValueValidator(5)], verbose_name='уровень')
#     '''tu zrobić filtr z Employment i wybrać spisek podwładnych'''
#
#     def __str__(self):
#         return f"{self.departament}, {self.superior}"
#
#     class Meta:
#         verbose_name = 'список началников подразделении'
#         verbose_name_plural = 'список началников подразделении'
#         ordering = ['id']
#
#
# class Assignment(models.Model):
#     level = models.ForeignKey(Superiors, on_delete=models.CASCADE, verbose_name='начальник')
#     subordinate = models.ManyToManyField(Personnel, verbose_name='подчиненный')
#
#     def __str__(self):
#         return f"{self.level}, {self.subordinate}"
#
#     class Meta:
#         verbose_name = 'список подчиненных'
#         verbose_name_plural = 'список подчиненных'
#         ordering = ['id']

# class DataMixin:
#     pass
#
#
# class LoginUser(DataMixin, LoginView):
#     form_class = AuthentificationForm
#     template_name = 'app_calendar/login.html'
#

#
# # class EmployeeAssessment(models.Model):
#     pass
#
#
# class RecruitmentEmployees(models.Model):
#     pass
#
#
# class EmployeeOrder(models.Model):
#     pass