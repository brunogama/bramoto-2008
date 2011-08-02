# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail, BadHeaderError

def main(request):
	return render_to_response('main.html', locals(), context_instance = RequestContext(request))

concessionarias = (
	('santa_maria', u'Santa Maria'),
	('cachoeira', u'Cachoeira do Sul'),
	('sao_borja', u'São Borja'),
	('santiago', u'Santiago'),
	('sao_gabriel', u'São Gabriel'),
)
class FormAssistencia(forms.Form):
	# error_css_class = 'error'
	# required_css_class = 'required'

	nome = forms.CharField(max_length=100, label=u'Nome completo')
	email = forms.EmailField(required=True, label=u'E-mail')
	telefone = forms.CharField(max_length=15, required=True)
	data = forms.DateField(label=u'Data para o serviço')
	concessionaria = forms.ChoiceField(choices=concessionarias, label=u'Concessionária para o serviço')
	texto = forms.Field(widget=forms.Textarea, label=u'Descrição do serviço')
	def enviar(self):
		pass


def assistencia(request):
	if request.method == 'POST':
		form = FormAssistencia(request.POST)

		if form.is_valid():
			form.enviar()
			mostrar = 'Dados enviados. Em breve iremos entrar em contato com você.'
			form = FormAssistencia()
	else:
		form = FormAssistencia()
	return render_to_response('oficina.html',
								{ 'form' : form },
								context_instance = RequestContext(request))
	
	
class FormContato(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	nome = forms.CharField(max_length=100, required=True)
	cidade = forms.CharField(max_length=100, required=True)
	telefone = forms.CharField(max_length=15, required=True)
	email = forms.EmailField(required=True, label=u'E-mail')
	comentario = forms.Field(widget=forms.Textarea, required=True, label=u'Comentários')

	def enviar(self):
		titulo = 'bramoto.com - Mensagem enviada pelo site'
		destino = ['bramotoolavo@terra.com.br', 'lamartine.souza@terra.com.br', 'bgamap@gmail.com', 'bramotoricardo@terra.com.br']
		texto = u"Nome: %(nome)s\n Cidade: %(cidade)s (Preenchido pelo Formulário)\n  Telefone: %(telefone)s\n E-mail: %(email)s\n Mensagem: %(comentario)s" % self.cleaned_data
		try:
			for to in destino:
				send_mail(titulo,texto,'contato@bramoto.com', list(to), fail_silently=False)
			pass
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		
def contato(request):
	print "current ======> %s" % request.get_host()
	pars = {}
	if request.method == 'POST':
		form = FormContato(request.POST)

		if form.is_valid():
			form.enviar()
			return HttpResponseRedirect('/contato/enviado/')
	else:
		form = FormContato()
	
	pars['form'] = form
	return render_to_response('contato.html',
							 pars,
							 context_instance = RequestContext(request))
							
							
def contato_enviado(request):
	pars = {}
	pars['mostrar'] = 'Sua mensagem foi enviada com sucesso.'
	
	return render_to_response('contato_enviado.html',
							 pars,
							 context_instance = RequestContext(request))