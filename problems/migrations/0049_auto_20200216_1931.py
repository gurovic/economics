# Generated by Django 3.0.2 on 2020-02-16 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0048_auto_20200131_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ожидает проверки'), (3, 'Проверено автоматически'), (2, 'Проверено учителем'), (0, 'Решение не сдано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(2, 'Тест с выбором одного ответа'), (4, 'Качественная задача'), (0, 'Задача'), (3, 'Тест с выбором нескольких ответов'), (1, 'Тест с ответом ДА/НЕТ')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(0, '---'), (1, 'Да'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(0, '---'), (1, 'Да'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='testsetassignment',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ожидает проверки'), (3, 'Проверено автоматически'), (2, 'Проверено учителем'), (0, 'Решение не сдано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='testsetassignment',
            name='test_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='problems.TestSet', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='testsubmit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(0, '---'), (1, 'Да'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
