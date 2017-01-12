# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Product(models.Model):
    name = models.CharField("Назва", max_length=20)
    price = models.PositiveIntegerField("Цiна")
    desc = models.TextField("Опис")

    class Meta:
        verbose_name_plural = 'Товари'


    def __unicode__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField("Имя", max_length=25)
    email = models.EmailField('Email')
    comment = models.TextField()
    product = models.ForeignKey(Product)


