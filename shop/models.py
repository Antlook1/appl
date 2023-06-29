from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'art': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Order(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house = models.CharField(max_length=50, verbose_name='Дом')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

