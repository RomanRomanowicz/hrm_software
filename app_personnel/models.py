import uuid
from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from app_company.models import *
from django.db import models
from django.contrib.auth.models import User, Group, Permission


class Employee(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee = models.OneToOneField('Personnel', on_delete=models.CASCADE, null=True, verbose_name='сотрудник')
    function = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='Должность')
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True,
                                    verbose_name='Подразделение фирмы')

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.employee}, {self.function}, {self.departament}"

    class Meta:
        ordering = ['employee']


class Personnel(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женшина')
    ]

    """uuid nie wspólpracuje z html przy wprowadzeniu danych powinno nastąpić automatyczne pobranie danych tj. Unique ID; do sprawdzenia później"""
    # id_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    first_name = models.CharField(max_length=40, verbose_name='Имя')
    fathers_name = models.CharField(max_length=40, null=True, blank=True, verbose_name='Отчество')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name='фото сотрудника')
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    email = models.EmailField(max_length=40, null=True, blank=True, verbose_name='e-mail')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='телефон')
    is_acceptance = models.BooleanField(default=True, verbose_name='Zatwierdzić')

    def get_absolute_url(self):
        return reverse('personnel', kwargs={'slug': self.slug})


    def __str__(self):
        if self.fathers_name is None:
            return f"{self.last_name}, {self.first_name}"
        return f"{self.last_name}, {self.first_name}, {self.fathers_name}"


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

    employee = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True, verbose_name='сотрудник')
    contract = models.CharField(max_length=2, choices=CONTRACTS, verbose_name='тип договора')
    employment_date_beginning = models.DateField(verbose_name='дата начала работы')
    employment_date_ending = models.DateField(blank=True, null=True, verbose_name='дата окончания контракта')
    # contract_for_an_indefinite_period = models.BooleanField(employment_date_ending)
    salary = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Размер зар. п.')
    uploadedFile = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='скану документов', null=True, blank=True)
    uploadedFile_date = models.DateField(verbose_name='дата годности документа', null=True, blank=True)
    education_remarks = models.TextField(blank=True, null=True, verbose_name='замечания по образованию')
    deadline = models.DateField(blank=True, null=True, verbose_name=' срок устрониения')

    def get_absolute_url(self):
        return reverse('employment-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.employee}"

    class Meta:
        verbose_name = 'Трудоустройство'
        verbose_name_plural = 'Трудоустройство'
        ordering = ['employee']


class PersonnelData(models.Model):
    employee = models.OneToOneField(Personnel, on_delete=models.CASCADE, primary_key=True, verbose_name='сотрудник')
    born = models.DateField(verbose_name='День рождения')
    birth_place = models.CharField(max_length=50, verbose_name='Место рождения')
    birth_country = models.CharField(max_length=50, verbose_name='Страна рождения')
    '''living'''
    country = models.CharField(max_length=50, verbose_name='Страна постоянного проживания')
    city = models.CharField(max_length=50, verbose_name='Город постоянного проживания')
    post_code = models.CharField(max_length=50, verbose_name='Почтовый индекс')
    street = models.CharField(max_length=100, verbose_name='Улица')
    street_number = models.IntegerField(verbose_name='Номер дома')
    house_number = models.IntegerField(blank=True, null=True, verbose_name='Номер квартиры')
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
    uploadedFile_date = models.DateField(blank=True, null=True, verbose_name='дата годности документа')
    is_acceptance = models.BooleanField(default=True, verbose_name='Zatwierdzić')

    def __str__(self):
        return f"{self.employee}"

    class Meta:
        verbose_name = 'Личные данные'
        verbose_name_plural = 'Личные данные'
        ordering = ['employee']


class Delegation(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    employee = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='сотрудник')
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cause = models.TextField(verbose_name='цель командировки')
    date_start = models.DateField(verbose_name='дата выезда')
    date_end = models.DateField(verbose_name='дата возвращения')
    departure_reason = models.CharField(max_length=150, verbose_name='Основание выезда')
    scan_of_documents = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True,
                                         verbose_name='Приказ о направлении сотрудника в командировку')

    class Meta:
        verbose_name = 'командировка'
        verbose_name_plural = 'командировка'
        ordering = ['date_start']
        # permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

    def __str__(self):
        return '%s (%s)' % (self.id, self.employee)


class Vacation(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    employee = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_start = models.DateField(verbose_name='Дата начала отпуска')
    date_end = models.DateField(verbose_name='Дата окончания отпуска')
    is_acceptance = models.BooleanField(default=True, verbose_name='Согласовано')

    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуск'
        ordering = ['date_start', 'is_acceptance']
        # permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

    def __str__(self):
        return '%s (%s)' % (self.id, self.employee)


class DailyReport(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    employee = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник')
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_start = models.DateTimeField(verbose_name='Дата и время начала работы', default=datetime.now)
    date_end = models.DateTimeField(verbose_name='Дата и время окончания работы', default=datetime.now)
    report = models.TextField(verbose_name='Ежедневный отчет')

    class Meta:
        verbose_name = 'Ежедневный отчет'
        verbose_name_plural = 'Ежедневный отчет'
        ordering = ['date_start',]
        # permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

    def __str__(self):
        return '%s (%s)' % (self.id, self.employee)
