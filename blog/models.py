from django.db import models

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    TYPE_PRINTER = (
        ('МФУ', 'МФУ'),
        ('Лазерный', 'Лазерный'),
        ('Цветной', 'Цветной'),
    )

    title = models.CharField(null=True, max_length=100, verbose_name='Название принтера')
    image = models.ImageField(null=True, upload_to='', verbose_name='Загрузите фото')
    description = models.TextField(null=True, blank=True, verbose_name='Дайте описание')
    type_printer = models.CharField(null=True, max_length=100, choices=TYPE_PRINTER,  verbose_name='выебрите модель')
    cost = models.PositiveIntegerField(null=True, verbose_name='Укажите цену')
    date_start = models.DateField(null=True, verbose_name='Укажите дату изготовления' )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Название принтера {self.title}- \n'
                f'Цена принтера {self.cost}')