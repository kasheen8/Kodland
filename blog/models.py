from django.db import models
from datetime import datetime

class Post(models.Model):
    """Посты"""
    title = models.CharField("Название", max_length=150)
    text = models.CharField("Текст", max_length=2000)
    image = models.ImageField("Иллюстрация", upload_to="image/")
    date = models.DateTimeField("Дата публикации", default=datetime.today())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        app_label = 'blog'

