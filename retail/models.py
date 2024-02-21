from django.core.exceptions import ValidationError
from django.db import models

from config import settings


class Contact(models.Model):
    email = models.EmailField(verbose_name='Почта звена сети')
    country = models.CharField(max_length=120, verbose_name='Страна нахождения звена сети', **settings.NULLABLE)
    city = models.CharField(max_length=120, verbose_name='Город нахождения звена сети', **settings.NULLABLE)
    street = models.CharField(max_length=120, verbose_name='Улица нахождения звена сети', **settings.NULLABLE)
    number = models.PositiveSmallIntegerField(verbose_name='Номер дома звена сети', **settings.NULLABLE)

    def __str__(self):
        return f'Адрес: {self.country}, {self.city}, {self.street}, {self.number}'

    class Meta:
        verbose_name = 'Контакт звена сети'
        verbose_name_plural = 'Контакты звена сети'


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Названия продукта произведенного звеном сети')
    type = models.CharField(max_length=120, verbose_name='Модель продукта произведенного звеном сети',
                            **settings.NULLABLE)
    release = models.DateField(verbose_name='Дата выхода продукта на рынок', **settings.NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт звена сети'
        verbose_name_plural = 'Продукты звена сети'


class UnionChain(models.Model):
    class LevelUnion(models.IntegerChoices):
        FACTORY = 0, 'Завод'
        RETAIL_CHAIN = 1, 'Розничная сеть'
        SOLE_PROPRIETOR = 2, 'Индивидуальный предприниматель'

    name = models.CharField(max_length=120, verbose_name='Название звена сети')
    level_union = models.PositiveSmallIntegerField(choices=LevelUnion.choices, verbose_name='Уровень звена сети')
    level_in_retail = models.PositiveSmallIntegerField(verbose_name='Уровень звена по отношению к поставщику',
                                                       **settings.NULLABLE)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name='Адрес звена сети',
                                related_name='contact')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт произведенный звеном сети',
                                related_name='product')
    supplier = models.ForeignKey('UnionChain', on_delete=models.SET_NULL, verbose_name='Поставщик от звена сети',
                                 **settings.NULLABLE)
    debt = models.DecimalField(default=0, max_digits=15, decimal_places=2,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания задолженности')

    def __str__(self):
        return f"{self.name}. Уровень: {self.level_union}"

    def save(self, *args, **kwargs):
        # для сохранения уровня в сети при отношении к поставщику
        sup = self.supplier
        lu = self.level_union
        diff_lvl = 0
        if sup is None or lu is None:
            pass
        elif sup and lu:
            diff_lvl = lu - sup.level_union
        self.level_in_retail = diff_lvl
        super(UnionChain, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
