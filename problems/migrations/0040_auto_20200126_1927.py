# Generated by Django 3.0.2 on 2020-01-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0039_auto_20200126_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ожидает проверки'), (2, 'Проверено учителем'), (3, 'Проверено автоматически'), (0, 'Решение не сдано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(2, 'Тест с выбором одного ответа'), (4, 'Качественная задача'), (1, 'Тест с ответом ДА/НЕТ'), (0, 'Задача'), (3, 'Тест с выбором нескольких ответов')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(0, '---'), (2, 'Нет'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='verdict',
            field=models.IntegerField(choices=[(-1, 'Не проверено учителем'), (0, 'Неверное решение'), (1, 'Частично верное решение'), (2, 'Верное решение с недочетами'), (3, 'Верное решение')], default=-1, verbose_name='Результат проверки учителем'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(0, '---'), (2, 'Нет'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
