# Create your views here.
import datetime
from django.contrib.sitemaps import Sitemap

# changefreq = always hourly daily weekly monthly yearly never

prioridade = 1

class MainSitemap(Sitemap):
	priority = prioridade
	location = '/'
	lastmod = datetime.datetime.now()
	changefreq = 'never'
	
	def items(self):
		return [self]

class MotosSitemap(Sitemap):
	priority = prioridade
	location = '/motos/'
	lastmod = datetime.datetime.now()
	changefreq = 'never'

	def items(self):
		return [self]

class AssistenciaSitemap(Sitemap):
	priority = prioridade
	location = '/oficina/assistencia-tecnica/'
	lastmod = datetime.datetime.now()
	changefreq = 'never'

	def items(self):
		return [self]		


class PecasSitemap(Sitemap):
	priority = prioridade
	location = '/oficina/pecas/'
	lastmod = datetime.datetime.now()
	changefreq = 'daily'

	def items(self):
		return [self]

class BoutiqueSitemap(Sitemap):
	priority = prioridade
	location = '/produtos/boutique/'
	lastmod = datetime.datetime.now()
	changefreq = 'daily'

	def items(self):
		return [self]		

class FinanciamentoSitemap(Sitemap):
	priority = prioridade
	location = '/produtos/financiamento/'
	lastmod = datetime.datetime.now()
	changefreq = 'daily'

	def items(self):
		return [self]		

class CNHSitemap(Sitemap):
	priority = prioridade
	location = '/produtos/consorcio-nacional-honda/'
	lastmod = datetime.datetime.now()
	changefreq = 'never'

	def items(self):
		return [self]
		
		
class ContatoSitemap(Sitemap):
	priority = prioridade
	location = '/contato/'
	lastmod = datetime.datetime.now()
	changefreq = 'never'
	
	def items(self):
		return [self]