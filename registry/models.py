from django.db import models

from django.urls import reverse


class Hospital(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Наименование учреждения')

    slug = models.SlugField(max_length=150,
                            unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Наименование учреждения'
        verbose_name_plural = 'Наименование учреждения'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    hospital = models.ForeignKey(Hospital,
                                 related_name='purchase',
                                 on_delete=models.CASCADE,
                                 verbose_name='Наименование учреждения')

    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='Объект закупки')

    slug = models.SlugField(max_length=200,
                            db_index=True)

    price = models.DecimalField(max_digits=15,
                                decimal_places=2,
                                verbose_name='Начальная цена контракта', null=True)

    signed = models.DateField(verbose_name='Направлено в Депфин')

    returned = models.DateField(verbose_name='Получено от Депфина')

    transferred = models.DateField(verbose_name='Направлено в учреждение')

    class Meta:
        ordering = ('name', 'price')
        index_together = (('id', 'slug'),)
        verbose_name = 'Закупки'
        verbose_name_plural = 'Закупки'

    def __str__(self):
        return self.name
