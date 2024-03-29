# Generated by Django 3.0.2 on 2020-01-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0036_auto_20200126_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(1, 'Решение не проверено'), (0, 'Решение не сдано'), (2, 'Решение проверено')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(0, 'Задача'), (1, 'Тест с ответом ДА/НЕТ'), (3, 'Тест с выбором нескольких ответов'), (2, 'Тест с выбором одного ответа'), (4, 'Качественная задача')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='right',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Верный ответ'),
        ),
    ]
