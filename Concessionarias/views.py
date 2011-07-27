# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Loja

def loja(request, slug):
	lojas = Loja.objects.all()
	loja = get_object_or_404(Loja, slug=slug)
	return render_to_response('concessionaria.html',
	 							locals(),
								context_instance = RequestContext(request))