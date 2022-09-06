# Generated by Django 4.1 on 2022-09-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departament', models.CharField(max_length=150, verbose_name='подразделение фирмы')),
            ],
            options={
                'verbose_name': 'подразделение фирмы',
                'verbose_name_plural': 'подразделение фирмы',
                'ordering': ['id'],
            },
        ),
    ]
