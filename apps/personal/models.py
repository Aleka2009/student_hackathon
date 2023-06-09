from django.db import models

from apps.prof.models import Profile


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'


QUARTER_CHOICES = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)
class PersonalFile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль', related_name='personal')

    class Meta:
        verbose_name = 'Личное дело'
        verbose_name_plural = 'Личное дело'


class Grade(models.Model):
    grade = models.IntegerField(verbose_name='класс')
    personal_file = models.ForeignKey(PersonalFile, on_delete=models.CASCADE, verbose_name='класс инфо', related_name='class_info')


    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Annual(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name='предмет')
    quarter_1 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_1')
    quarter_2 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_2')
    quarter_3 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_3')
    quarter_4 = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='четверть_4')
    quarter_final = models.IntegerField(choices=QUARTER_CHOICES, verbose_name='итоговая')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='годовая', related_name='annual')

    class Meta:
        verbose_name = 'Годовая'
        verbose_name_plural = 'Годовые'