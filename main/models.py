
# отвечает за базу данных
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# статусф: (открытый, закрытый, черновик)
# Каждый вариан выбора представляется в виде кортежа из 2 элементов :
# (ключ, текст) ключ хранится в БД(open, close, draft), а текст используется для отображения данных
STATUS_CHOICES = (
    ('open', 'Открытое'),
    ('closed', 'Закрытое'),
    ('draft', 'Черновик')
)


class Publication(models.Model):
    """Классы, которые наследуются от models.Model являются моделями, то есть отвечаеют за связь с БД через ORM,
    в БД будет создана таблица с указанными полями"""
    title = models.CharField('Заголовок', max_length=255)
    # CharField - VARCHAR(), обязательное свойство max_length
    text = models.TextField('Текст')
    # TextField - Text(), поле без ограничений в длине
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES)
    # choices - жестко ограниченные варианты выбора, то есть невозможно вписывать другие варианты
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pubs', verbose_name='Объявление')
    # ForeignKey - поле для связи с другой моделью, обязательные свойства:
    # модель, on_delete(определяет, что произойдет с объявлением,если удалить автора из БД)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    # DateTimeField - TIMESTAMP, auto_now_add - время задается при добавлении записи,
    # auto_now - время задается при изменениии записи
    updated_at = models.DateTimeField('Дата редактирования', auto_now=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявление'

    def __str__(self):
        return self.title


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments',
                                    verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарий')
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return f'{self.publication} -> {self.user}'
