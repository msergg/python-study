# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class OnlyAvailable(models.Manager):
    def get_queryset(self):
        return super(OnlyAvailable, self).get_queryset().filter(is_avaiable=True)

    def set_all_available(self):
        Product.objects.update(is_available=True)

# http://ccbv.co.uk/

class Product(models.Model):
    name = models.CharField("Назва", max_length=20)
    price = models.PositiveIntegerField("Цiна")
    desc = models.TextField("Опис")
    is_avaiable = models.BooleanField(default=True)

    objects = models.Manager()
    available = OnlyAvailable()




    class Meta:
        verbose_name_plural = 'Товари'


    def __unicode__(self):
        return self.name

    def set_available(self, f):
        self.is_avaiable = f


class Comment(models.Model):
    name = models.CharField("Имя", max_length=25)
    email = models.EmailField('Email')
    comment = models.TextField()
    product = models.ForeignKey(Product)


