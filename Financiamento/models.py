# -*- coding: utf-8 -*-
from django.db import models

class Moto(models.Model):
    modelo = models.CharField(max_length=30,help_text='Modelo da moto')
    preco = models.FloatField(verbose_name=u'Preço')
    data_add = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('modelo',)
    def __unicode__(self):
        return self.modelo