# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

upload_path = 'sistemas.public/Concessionarias/Loja/'
nome_help = u'No caso de necessitar de um nome complementar. Exemplo: "Bramoto Seminovas"'

class Loja(models.Model):
	cidade = models.CharField(max_length = 50)
	nome = models.CharField(blank=True, max_length=100, help_text=nome_help)
	endereco = models.CharField(verbose_name = u'Endereço', max_length = 150)
	telefone = models.CharField(max_length = 15)
	imagem = models.ImageField(verbose_name = 'Fachada', upload_to = upload_path)
	legenda_imagem = models.CharField(verbose_name = 'Legenda Imagem', max_length = 150)
	slug = models.SlugField(max_length = 100, blank = True, unique=True, editable=False)
	created = models.DateTimeField(blank=True, auto_now_add=True,verbose_name=u'data de criação')
	link_externo = models.CharField(blank=True, max_length=150, verbose_name=u'Link Externo')
	link_externo_label = models.CharField(blank=True, max_length=100, verbose_name=u'Texto para link externo')
	
	def __unicode__(self):
		if self.nome:
			return u'Loja %s (%s)' % (self.nome, self.cidade)
		else: 
			return u'Loja %s' % (self.cidade)
			
	def get_absolute_url(self):
		return reverse('loja_slug', args=[self.slug,])

	class Meta:
		ordering = ('cidade',)


def LojaPreSave(signal, instance, sender, **kwargs):
	if instance.nome:
		slug_string = instance.nome + ' (' + instance.cidade + ')'
		instance.slug = slugify(slug_string)
	else:
		instance.slug = slugify(instance.cidade)

signals.pre_save.connect(LojaPreSave, sender=Loja)