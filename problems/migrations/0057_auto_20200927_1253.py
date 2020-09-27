# Generated by Django 2.1.15 on 2020-09-27 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0056_auto_20200927_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupteacher',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='groupteacher',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_group', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(3, 'Тест с выбором нескольких ответов'), (4, 'Качественная задача'), (0, 'Задача'), (2, 'Тест с выбором одного ответа'), (1, 'Тест с ответом ДА/НЕТ')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (0, '---'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (0, '---'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='testsubmit',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (0, '---'), (1, 'Да')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
    ]
