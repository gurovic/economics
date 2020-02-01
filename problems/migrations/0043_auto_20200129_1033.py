# Generated by Django 3.0.2 on 2020-01-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0042_auto_20200126_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Решение не сдано'), (2, 'Проверено учителем'), (3, 'Проверено автоматически'), (1, 'Ожидает проверки')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(2, 'Тест с выбором одного ответа'), (4, 'Качественная задача'), (3, 'Тест с выбором нескольких ответов'), (0, 'Задача'), (1, 'Тест с ответом ДА/НЕТ')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(blank=True, choices=[(2, 'Нет'), (0, '---'), (1, 'Да')], default=None, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (0, '---'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('problems', models.ManyToManyField(to='problems.Problem')),
            ],
        ),
    ]
