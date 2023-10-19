from django.db import models


class Quizzes(models.Model):
    """Модель вопросов викторины."""
    question_id = models.IntegerField(
        verbose_name='ID вопроса',
        unique=True
    )
    question_text = models.CharField(
        verbose_name='Текст вопроса',
        unique=True,
        max_length=350
    )
    answer_text = models.CharField(
        verbose_name='Ответ на вопрос',
        max_length=150
    )
    date = models.DateTimeField(
        verbose_name='Дата создания вопроса'
    )
    count = models.IntegerField(
        null=True
    )
