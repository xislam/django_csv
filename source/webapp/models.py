from django.db import models


class ModelCSV(models.Model):
    code = models.CharField(max_length=10, verbose_name="Код")
    name = models.CharField(max_length=50, verbose_name="Наименование")
    level1 = models.CharField(max_length=100, verbose_name="Левел 1")
    level2 = models.CharField(max_length=100, verbose_name="Левел 2")
    level3 = models.CharField(max_length=100, verbose_name="Левел 3")
    price = models.CharField(max_length=50, verbose_name="цена")
    sp_price = models.CharField(max_length=50, verbose_name="ценаСП")
    quantity = models.CharField(max_length=50, verbose_name="Количество")
    property_fields = models.CharField(max_length=50, verbose_name="Поля свойств")
    joint_purchases = models.CharField(max_length=150, verbose_name="Совместныйе покупки")
    unit_of_measure = models.CharField(max_length=150, verbose_name="Еденица измерения")
    picture = models.CharField(max_length=225, verbose_name="Картина")
    display_on_main_page = models.CharField(max_length=225, verbose_name="Выводить на главную")
    description = models.CharField(max_length=225, verbose_name="Описание")

    def __str__(self):
        return self.code
