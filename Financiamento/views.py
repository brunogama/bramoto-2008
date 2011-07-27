# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django import forms
from bramoto.Produtos.models import Moto


def financiamento(request):
	motos = Moto.objects.all()
	return render_to_response('financiamento.html', 
							  { 'motos' : motos },
							  context_instance = RequestContext(request))