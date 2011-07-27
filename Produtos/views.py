# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Artigo

def pecas(request):
	artigos = Artigo.objects.filter(categoria='pecas')
	return render_to_response('oficina-pecas.html',
								{ 'artigos' : artigos },
								context_instance = RequestContext(request))
	
def boutique(request):
	artigos = Artigo.objects.filter(categoria='boutique')
	return render_to_response('boutique.html',
								{ 'artigos' : artigos },
								context_instance = RequestContext(request))