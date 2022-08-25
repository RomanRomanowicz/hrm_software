# Generated by Django 4.1 on 2022-08-25 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('fathers_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='фото сотрудника')),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женшина')], max_length=1, verbose_name='Пол')),
                ('email', models.EmailField(blank=True, max_length=25, null=True, verbose_name='e-mail')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='телефон')),
                ('is_acceptance', models.BooleanField(default=True, verbose_name='Zatwierdzić')),
            ],
            options={
                'verbose_name': 'сотрудника',
                'verbose_name_plural': 'сотрудники',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('number_file', models.AutoField(primary_key=True, serialize=False, verbose_name='№ папки')),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_company.orgstructure', verbose_name='подразделение фирмы')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_personnel.personnel', verbose_name='сотрудник')),
                ('function', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_company.function', verbose_name='должность')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
                'ordering': ['employee'],
            },
        ),
    ]
