# Generated by Django 3.0.2 on 2020-03-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0052_auto_20200216_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(2, 'Проверено учителем'), (0, 'Решение не сдано'), (3, 'Проверено автоматически'), (1, 'Ожидает проверки')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(4, 'Качественная задача'), (1, 'Тест с ответом ДА/НЕТ'), (2, 'Тест с выбором одного ответа'), (3, 'Тест с выбором нескольких ответов'), (0, 'Задача')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='testsetassignment',
            name='status',
            field=models.IntegerField(choices=[(2, 'Проверено учителем'), (0, 'Решение не сдано'), (3, 'Проверено автоматически'), (1, 'Ожидает проверки')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='testsubmit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
