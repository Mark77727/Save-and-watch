from django.db import models

from django.urls import reverse


class Hospital(models.Model):
    name = models.CharField(max_length=150,
                            db_index=True,
                            verbose_name='Наименование учреждения')

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
                                 verbose_name='Наименование учреждения', blank=True, null=True)

    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='Объект закупки')

    price = models.DecimalField(max_digits=15,
                                decimal_places=2,
                                verbose_name='Начальная цена контракта')

    signed = models.DateField(verbose_name='Направлено в Депфин', blank=True, null=True)

    returned = models.DateField(verbose_name='Получено от Депфина', blank=True, null=True)

    transferred = models.DateField(verbose_name='Направлено в учреждение', blank=True, null=True)

    class Meta:
        ordering = ('name', 'price')
        index_together = (('id'),)
        verbose_name = 'Закупки'
        verbose_name_plural = 'Закупки'

    def __str__(self):
        return self.name
