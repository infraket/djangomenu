from django.db import models


class Menu(models.Model):
    """
    Таблица Меню.
    title - Название меню.
    slug - Слаг названия меню.
    """
    title = models.CharField(max_length=255, unique=True,
                             verbose_name='Заголовок меню')
    slug = models.SlugField(max_length=255, verbose_name="Slug меню")

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class Item(models.Model):
    """
    Таблица элементов меню.
    title - Название элемента(подменю).
    slug - Слаг элемента(подменю).
    menu - К какому меню относится элемент.
    parent - Родительский элемент.
    """
    title = models.CharField(max_length=255, verbose_name='Подменю')
    slug = models.SlugField(max_length=255, verbose_name="Slug подменю")
    menu = models.ForeignKey(Menu, blank=True, related_name='items',
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='childrens',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'

    def __str__(self):
        return self.title
