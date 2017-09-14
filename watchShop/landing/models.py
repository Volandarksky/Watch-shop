# -- coding: utf-8 --

from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"Name: %s, Email: %s" % (self.name, self.email)

    class Meta:
        verbose_name = "MySubscriber"
        verbose_name_plural = "MySubscribers"
