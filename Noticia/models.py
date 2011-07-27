# -*- coding: utf-8 -*-
from django.db import models
help = {
	'chamada' : u'Título da notícia, atualmente não aparece no layout do site.',
	'texto' : u'Para gerar novos parágrafos deixar uma linha de intervalo.'
}
class Noticias(models.Model):
	"""(Noticias description)"""
	chamada = models.CharField(blank=False, max_length=100, default='', help_text=help['chamada'])
	texto = models.TextField(blank=False, help_text = help['texto'])
	created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=u'Data de publicação')
	
	class Meta:
		ordering = ('-created',)
		verbose_name = u'Notícia'

	def __unicode__(self):
		return self.chamada