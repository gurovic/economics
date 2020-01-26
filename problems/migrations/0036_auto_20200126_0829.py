# Generated by Django 3.0.2 on 2020-01-26 08:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0035_auto_20200123_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AddField(
            model_name='submit',
            name='multiplechoice_answer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Выбор ответов'),
        ),
        migrations.AddField(
            model_name='submit',
            name='yesno_answer',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ответ (ДА/НЕТ)'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Решение не сдано'), (1, 'Решение не проверено'), (2, 'Решение проверено')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.IntegerField(choices=[(3, 'Тест с выбором нескольких ответов'), (4, 'Качественная задача'), (2, 'Тест с выбором одного ответа'), (1, 'Тест с ответом ДА/НЕТ'), (0, 'Задача')], default=0, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='yesno_answer',
            field=models.IntegerField(choices=[(2, 'Нет'), (1, 'Да'), (0, '---')], default=0, verbose_name='Ответ ДА/НЕТ'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='answer_autoverdict',
            field=models.BooleanField(blank=True, null=True, verbose_name='Результат автоматической проверки'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='solution',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Решение'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='verdict',
            field=models.IntegerField(choices=[(-1, 'Решение не проверено'), (0, 'Неверное решение'), (1, 'Частично верное решение'), (2, 'Верное решение с недочетами'), (3, 'Верное решение')], default=-1, verbose_name='Результат проверки учителем'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='right',
            field=models.IntegerField(choices=[(2, 'Нет'), (1, 'Да'), (0, '---')], default=0, verbose_name='Верный ответ'),
        ),
    ]
