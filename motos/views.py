# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from bramoto.Produtos.models import Moto, MotoExtraInfo


def motos(request):
	a = [x['extra'] for x in Moto.objects.values('extra').order_by('cilindradas').distinct()]
	motos = []
	for x in a:
		motos.append(MotoExtraInfo.objects.get(id=x))
	
	return render_to_response('motos.html',
							{ 'motos' : motos },
							context_instance = RequestContext(request))