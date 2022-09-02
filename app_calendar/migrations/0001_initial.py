# Generated by Django 4.1 on 2022-09-01 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.TextField(verbose_name='цель командировки')),
                ('date_start', models.DateField(verbose_name='дата выезда')),
                ('date_end', models.DateField(verbose_name='дата возвращения')),
                ('departure_reason', models.CharField(max_length=150, verbose_name='Основание выезда')),
                ('scan_of_documents', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d', verbose_name='Приказ о направлении сотрудника в командировку')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_personnel.personnel', verbose_name='сотрудник')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'командировка',
                'verbose_name_plural': 'командировка',
                'ordering': ['date_start'],
                'permissions': [('can_deliver_pizzas', 'Can deliver pizzas')],
            },
        ),
    ]
