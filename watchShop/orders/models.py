# -*- coding: utf-8 -*-
from django.db import models
from products.models import Product
from django.db.models.signals import post_save

# Create your models here.



class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



class Order(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=30, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=130, blank=True, null=True, default=None)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb total price for all products in order

    status = models.ForeignKey(Status)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"Заказ: %s, статус: %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)

    nmb = models.IntegerField(default=1)
    pricePerItem = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        pricePerItem = self.product.price
        self.pricePerItem = pricePerItem
        self.totalPrice = self.nmb * pricePerItem

        super(ProductInOrder, self).save( *args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.totalPrice

    instance.order.totalPrice = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)

    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)

    nmb = models.IntegerField(default=1)
    pricePerItem = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return u"%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        pricePerItem = self.product.price
        self.pricePerItem = pricePerItem
        self.totalPrice = int(self.nmb) * pricePerItem

        super(ProductInBasket, self).save( *args, **kwargs)
