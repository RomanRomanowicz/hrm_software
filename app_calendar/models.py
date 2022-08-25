import uuid

from django.db.models.expressions import RawSQL

from app_personnel.models import *
from app_company.models import *
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Delegation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name='сотрудник')
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    destination = models.TextField(verbose_name='цель командировки')
    date_start = models.DateField(verbose_name='дата выезда')
    date_end = models.DateField(verbose_name='дата возвращения')
    departure_reason = models.CharField(max_length=150, verbose_name='Основание выезда')
    scan_of_documents = models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True,
                                         verbose_name='Приказ о направлении сотрудника в командировку')


    class Meta:
        verbose_name = 'командировка'
        verbose_name_plural = 'командировка'
        ordering = ['date_start']
        permissions = [('can_deliver_pizzas', 'Can deliver pizzas')]

    def __str__(self):
        return '%s (%s)' % (self.id, self.employee)


# class VisibleManager(models.Manager):
#     def __int__(self, username, model):
#         self.username = username
#         self.employee = Employee.objects.get_for_model(model)
#         self.model = model
#         self.name = 'visible_for_{}'.format(username)
#
#     def get_queryset(self):
#         return super().get_queryset().filter(id__in=self._get_visible_filter())
#
#     def _get_visible_filter(self):
#         return RawSQL("select object_id from aclapp_acl where username = %s and model_conent_type = %s",
#                       (self.username, self.content_type.id,))
#
#
# def accessible_objects(self, user):
#     return VisibleManager(user.usename, Delegation)





    # @property
    # def is_overdue(self):
    #     if self.employee and date.today() > self.employee:
    #         return True
    #     return False





# class DepartamentE(models.Model):
#     dep = models.OneToOneField(OrgStructure, on_delete=models.CASCADE, verbose_name='подразделение фирмы')
#     superior = models.ForeignKey(Personnel, on_delete=models.CASCADE, verbose_name='начальник')
#     function = models.ForeignKey(Function, on_delete=models.CASCADE, verbose_name='должность')
#
#     def __str__(self):
#         return f"{self.dep}, {self.function}, {self.superior}"
#
#     class Meta:
#         verbose_name = 'Распределение'
#         verbose_name_plural = 'Распределение'
#         ordering = ['id']

#
# class DepSubordinate(models.Model):
#     superior = models.ForeignKey(DepartamentE, on_delete=models.CASCADE, verbose_name='начальник')
#     subordinate = models.ManyToManyField(Personnel, verbose_name='сотрудник')
#
#     def __str__(self):
#         return f"{self.superior}, {self.subordinate}"
#
#     class Meta:
#         verbose_name = 'Распределение'
#         verbose_name_plural = 'Распределение'
#         ordering = ['id']
#

# class InstructionE(models.Model):
#     employee = models.ManyToManyField(Personnel, verbose_name='сотрудник')
#     instr = models.ForeignKey(InstructionList, on_delete=models.CASCADE, verbose_name='направление на обучение')
#
#     def __str__(self):
#         return f"{self.employee}, {self.instr}"
#
#     class Meta:
#         verbose_name = 'направление на обучение'
#         verbose_name_plural = 'направление на обучение'
#         ordering = ['id']

#
# class Delegation(models.Model):
#     employee = models.ForeignKey(Personnel, on_delete=models.CASCADE, verbose_name='сотрудник')
#     departament = models.OneToOneField(Departament, on_delete=models.CASCADE, verbose_name='Наменование подразделения')
#     destination = models.TextField(verbose_name='цель командировки')
#     date_start = models.DateField(verbose_name='дата выезда')
#     date_end = models.DateField(verbose_name='дата возвращения')
#     departure_reason = models.CharField(max_length=150, verbose_name='Основание выезда')
#     delegation = models.FileField(upload_to='files/%Y/%m/%d', verbose_name='Приказ о направлении сотрудника в командировку', null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.employee}, {self.departament}"
#
#     class Meta:
#         verbose_name = 'направление на обучение'
#         verbose_name_plural = 'направление на обучение'
#         ordering = ['id']
