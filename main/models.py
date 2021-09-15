
# отвечает за базу данных
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# статусф: (открытый, закрытый, черновик)
STATUS_CHOICES = (
    ('open', 'Открытое'),
    ('closed', 'Закрытое'),
    ('draft', 'Черновик')
)


class Publication(models.Model):

    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pubs', verbose_name='Объявление')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
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
