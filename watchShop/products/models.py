# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'

class ProductDiscount(models.Model):
    is_active = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" % self.discount

    class Meta:
        verbose_name = 'Скидка товара'
        verbose_name_plural = 'Скидки товаров'

class Product(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    discountClass = models.ForeignKey(ProductDiscount, blank=True, null=True, default=None)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=False)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"%s, %s руб." % (self.name, self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='product_img/')

    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"%s" % self.id

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
