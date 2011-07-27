# -*- coding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField

# Create your models here.
CATEGORIAS = (
    ('pecas', u'Peças'),
    ('boutique','Boutique'),    
)

upload_path = 'sistemas.public/Produtos/Artigo/'

nome_help = u'Texto título que representará o produto.'
imagem_help = u'A imagem será redimensionada para um máximo de 499x492 pixels, mantendo as proporções.'
created_label = u'Data de criação'
tsizes = (
	(75,74),
	(499,492),
)

class Artigo(models.Model):
	nome = models.CharField(blank=False, max_length = 100, help_text = nome_help)
	imagem = ImageWithThumbsField(blank=False, upload_to = upload_path, sizes=tsizes, help_text=imagem_help)
	descricao = models.TextField(blank=True, verbose_name=u'descrição')
	valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
	parcelas = models.IntegerField(default=0, blank=True, null=True, verbose_name=u'Número de parcelas')
	valor_parcela = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=u'Valor das parcelas', blank=True, null=True)
	categoria = models.CharField(choices = CATEGORIAS, max_length = 10)
	created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=created_label)
	class Meta:
		ordering = ('categoria','nome',)
	def __unicode__(self):
		return self.nome


class Cilindradas(models.Model):
	"""(Cilindradas description)"""
	num_cilindros = models.IntegerField(blank=True, null=True, verbose_name=u'número de cilindros')
	created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=created_label)

	def __unicode__(self):
		return  u'%s' % (self.num_cilindros)
		
	class Meta:
		ordering = ( 'num_cilindros', )
		verbose_name_plural = u'Cilindradas'

class Categoria(models.Model):
	"""(Categoria description)"""

	nome = models.CharField(blank=False, max_length=100)
	created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=created_label)
	class Meta:
		ordering = ( 'nome', )
	def __unicode__(self):
		return self.nome


upload_path_moto = 'sistemas.public/Produtos/Moto/'
class MotoExtraInfo(models.Model):
	"""(MotoExtraInfo description)"""
	
	nome = models.CharField(blank=False, max_length=100, help_text=u'Nome comum, da moto sem subdivisões (ESD, ES entre outras)', verbose_name=u'Nome comum')
	imagem = ImageWithThumbsField(blank=True, upload_to = upload_path_moto, sizes=tsizes, help_text=imagem_help, null=True)
	hotsite = models.URLField(blank=True, verify_exists=True)
	
	def __unicode__(self):
		return u"%s" % (self.nome)
		

class Moto(models.Model):
	"""Modelo representante de motos"""

	modelo = models.CharField(blank=False, max_length=100)
	valor = models.DecimalField(max_digits=10, decimal_places=2)
	ano = models.IntegerField(blank=True, null=True)
	caracteristicas = models.TextField(blank=True, verbose_name=u'características')
	categoria = models.ForeignKey(Categoria)
	cilindradas = models.ForeignKey(Cilindradas)
	created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=created_label)
	extra = models.ForeignKey(MotoExtraInfo)

	def __unicode__(self):
		return self.modelo