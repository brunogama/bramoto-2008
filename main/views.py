# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from bramoto.Noticia.models import Noticias
from bramoto.banners.models import Banner

def index(request):
	be = Banner.objects.filter(lado='esquerda').order_by('-created')[0]
	bd = Banner.objects.filter(lado='direita').order_by('-created')[0]
	noticia = Noticias.objects.all()[0]
	return render_to_response('main.html',
								{ 'noticia' : noticia, 'be' : be, 'bd' : bd },
								context_instance = RequestContext(request))