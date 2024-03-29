# Generated by Django 3.0.2 on 2020-01-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0038_auto_20200126_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Решение не сдано'), (2, 'Решение проверено'), (1, 'Решение не проверено')], default=0, verbose_name='Статус'),
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
            model_name='variant',
            name='right',
            field=models.BooleanField(default=False, verbose_name='Верный ответ'),
        ),
    ]
