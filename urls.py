from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf import settings
from Concessionarias.models import Loja
from bramoto.sitemap.views import MainSitemap, MotosSitemap, ContatoSitemap, AssistenciaSitemap, PecasSitemap, BoutiqueSitemap
from bramoto.sitemap.views import CNHSitemap, FinanciamentoSitemap


admin.autodiscover()

lojas = {
    'queryset': Loja.objects.all(),
    'date_field': 'created',
}

sitemaps = {
	'home' : MainSitemap,
    'concessionaria': GenericSitemap(lojas, priority=0.6),
	'motos' : MotosSitemap,
	'assistencia' : AssistenciaSitemap,
	'boutique' : BoutiqueSitemap,
	'CNH' : CNHSitemap,
	'pecas' : PecasSitemap,
	'financiamento' : FinanciamentoSitemap,
	'contato' : ContatoSitemap,
}



urlpatterns = patterns('',
	url(r'^concessionaria/(?P<slug>[\w_-]+)/$', 'bramoto.Concessionarias.views.loja', name='loja_slug'),
	url(r'^oficina/assistencia-tecnica/$', 'bramoto.Contato.views.assistencia', name='assistencia'),
	url(r'^oficina/pecas/$', 'bramoto.Produtos.views.pecas', name='pecas'),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^contato/$', 'bramoto.Contato.views.contato', name='contato'),
	url(r'^contato/enviado/$', 'bramoto.Contato.views.contato_enviado'),
	url(r'^produtos/boutique/$', 'bramoto.Produtos.views.boutique', name='boutique'),
	url(r'^produtos/financiamento/$', 'bramoto.Financiamento.views.financiamento', name='financiamento'),
	url(r'^$', 'bramoto.main.views.index', name='main'),
	url(r'^motos/$', 'bramoto.motos.views.motos', name='motos'),
	
)

urlpatterns += patterns('django.views.generic.simple',
	url(r'^produtos/consorcio-nacional-honda/$', 'direct_to_template', { 'template' : 'cnh.html'}, name='cnh'),
    url(r'^produtos/$', 'redirect_to', {'url': '/produtos/boutique/'}, name='produtos'),
    # url(r'^produto/(?P<slug>[\w_-]+)/$', 'redirect_to', {'url': '/produtos/%(slug)s/'}, name='produtos_slug'),
	# url(r'^motos/$', 'direct_to_template', { 'template' : 'motos.html'}, name='motos'),
)

urlpatterns += patterns('',
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	(r'^painel/', include(admin.site.urls)),
)