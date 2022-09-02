from django.db import models


class Departament(models.Model):
    departament = models.CharField(max_length=150, verbose_name='подразделение фирмы')

    def __str__(self):
        return f"{self.departament}"

    class Meta:
        verbose_name = 'подразделение фирмы'
        verbose_name_plural = 'подразделение фирмы'
        ordering = ['id']















""" funkcje to są grupy """

# class Function(models.Model):
#     # PRIMARY_EDUCATION = 'PE'
#     # SECONDARY_EDUCATION = 'SE'
#     # HIGHER_EDUCATION = 'HE'
#     # EDUCATION = [
#     #     (PRIMARY_EDUCATION, 'Начальное образование'),
#     #     (SECONDARY_EDUCATION, 'Среднее образование'),
#     #     (HIGHER_EDUCATION, 'Высшее образование')
#     # ]
#     function = models.CharField(max_length=150, verbose_name='должность')
#     # education = models.CharField(max_length=2, choices=EDUCATION, verbose_name='Необходимое образование для должности')
#
#     def __str__(self):
#         return f"{self.function}"
#
#     class Meta:
#         verbose_name = 'должность'
#         verbose_name_plural = 'должность'
#         ordering = ['id']
#
#
# # class Qualifications(models.Model):
#     qualifications = models.CharField(max_length=150, verbose_name='Квалификации')
#
#     def __str__(self):
#         return f"{self.qualifications}"
#
#     class Meta:
#         verbose_name = 'Квалификации'
#         verbose_name_plural = 'Квалификации'
#         ordering = ['id']



# class Vacation(models.Model):
#     function = models.ForeignKey(Function, on_delete=models.CASCADE, verbose_name='Должность')
#     vacation_limit = models.IntegerField(default='20', verbose_name='отпуск')
#     remote_work_limit = models.IntegerField(default='0',verbose_name='удаленная работа')
#
#     def __str__(self):
#         return f"{self.function}, {self.vacation_limit}, {self.remote_work_limit}"
#
#     class Meta:
#         verbose_name = 'отпуск и удаленная работа'
#         verbose_name_plural = 'отпуск'
#         ordering = ['id']
#

# class Delegation(models.Model):
#     function = models.ForeignKey(Function, on_delete=models.CASCADE)
#     delegation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='командировочные в BYN: ')
#     limit_journey = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Лимит аванса на поездку в BYN: ')
#     limit_hotel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Лимит аванса на гостинницу в BYN: ')
#     limit_payment_on_account = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Лимит аванса на день в BYN: ')
#
#     def __str__(self):
#         return f"{self.function}"
#
#     class Meta:
#         verbose_name = 'командировка'
#         verbose_name_plural = 'командировка'
#         ordering = ['id']




# class Level(models.Model):
#     function = models.ForeignKey(Function, on_delete=models.CASCADE)
#     is_function = models.BooleanField(default=True, verbose_name='dostęp')


# class InstructionList(models.Model):
#     instruction = models.TextField(verbose_name='Обучение')
#     start_date = models.DateField(verbose_name='Дата начала обучения')
#     send_date = models.DateField(verbose_name='Дата окончания обучения')
#
#     def __str__(self):
#         return f"{self.instruction}"
#
#     class Meta:
#         verbose_name = 'Обучение'
#         verbose_name_plural = 'Обучение'
#         ordering = ['id']



# class EmployeeAssessment(models.Model):
#     pass