# -*- encoding: utf-8 -*-

from django.db import models

banner_side = (
	('esquerda', 'Esquerda'),
	('direita', 'Direita'),
)

banner_path = 'sistemas.public/banners/'


class Banner(models.Model):
	titulo = models.CharField( max_length=100, verbose_name=u'Título', help_text=u'Título para representar o banner no sistema.' )
	banner = models.FileField(upload_to=banner_path, help_text=u'Arquivos permitidos *.jpg e *.swf')
	created = models.DateTimeField(blank=True, auto_now_add=True)
	lado = models.CharField(blank=False, max_length=100, choices = banner_side, help_text=u'Lado em que o banner irá aparecer no leiaute.')	
	uri = models.URLField(blank=False, verify_exists=True, verbose_name=u'Endereço', help_text=u'Endereço completo para onde o banner irá encaminhar o usuário. É necessário iniciar com "http://".')
	
	def __unicode__(self):
		return self.titulo
