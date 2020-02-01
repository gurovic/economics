# Generated by Django 3.0.2 on 2020-01-31 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0046_auto_20200131_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsetassignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Решение не сдано'), (2, 'Проверено учителем'), (1, 'Ожидает проверки'), (3, 'Проверено автоматически')], default=0, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='testsubmit',
            name='problem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='test_submits', to='problems.Problem', verbose_name='Задача'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Решение не сдано'), (2, 'Проверено учителем'), (1, 'Ожидает проверки'), (3, 'Проверено автоматически')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(2, 'Тест с выбором одного ответа'), (3, 'Тест с выбором нескольких ответов'), (1, 'Тест с ответом ДА/НЕТ'), (0, 'Задача'), (4, 'Качественная задача')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(blank=True, choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=None, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='testsubmit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(1, 'Да'), (0, '---'), (2, 'Нет')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
