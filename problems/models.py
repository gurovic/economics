from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Topic(models.Model):
    name = models.CharField('Название', max_length=200)
    parent = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='children', verbose_name='Предок', null=True, blank=True)
    order = models.IntegerField('Порядковый номер')
    leaf = models.BooleanField('Конечная вершина (можно привязывать задачи)', default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Problem(models.Model):
    name = models.CharField('Название', max_length=200)
    task = RichTextUploadingField('Условие')
    short_answer = models.CharField('Ответ (для автоматической проверки)', max_length=200, blank=True)
    # TODO long_answer =
    # TODO subproblem_answers

    solution = RichTextUploadingField('Решение', blank=True)

    # TODO author
    # TODO difficulty
    # TODO attributes: производная, парабола итп
    # TODO LOGS
    #   TODO pub_date = models.DateTimeField('date published')
    #   TODO edit_date = models.DateTimeField('date last editied')
    #   TODO pub_user =
    #   TODO edit_user =
    #   TODO pictures_quality : draft, final
    #   TODO text_quality: draft, final
    # TODO yes/no question
    # TODO ABCD answers (radiobuttons)
    # TODO checkboxes
    # TODO problem_type - стандартные, олимпиадные

    hint = RichTextUploadingField('Подсказка', blank=True)

    topics = models.ManyToManyField(Topic, related_name="problems", verbose_name='Темы')

    assignments = models.ManyToManyField(User, through='Assignment', through_fields=['problem', 'person'])



    def __str__(self):
        return "{}. {}. {}...".format(self.id, self.name, self.task[:30])

    class Meta:
        ordering = ['id']


class Assignment(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кому задано')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name='Задача')
    date_assigned = models.DateField('Когда задано', auto_now_add=True, blank=False)
    date_deadline = models.DateField('Сдать до', blank=True, null=True)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigner', verbose_name='Кем задано')

    def __str__(self):
        return "{} -> {}. {} {}".format(self.problem, self.person.id, self.person.last_name, self.person.first_name)

    class Meta:
        ordering = ['date_assigned']

