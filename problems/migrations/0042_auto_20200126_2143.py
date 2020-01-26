# Generated by Django 3.0.2 on 2020-01-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0041_auto_20200126_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(2, 'Проверено учителем'), (0, 'Решение не сдано'), (3, 'Проверено автоматически'), (1, 'Ожидает проверки')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(0, 'Задача'), (2, 'Тест с выбором одного ответа'), (1, 'Тест с ответом ДА/НЕТ'), (3, 'Тест с выбором нескольких ответов'), (4, 'Качественная задача')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(blank=True, choices=[(2, 'Нет'), (1, 'Да')], default=None, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
