# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Artigo, Categoria, Cilindradas, Moto, MotoExtraInfo

class ArtigoAdmin(admin.ModelAdmin):
	list_display = ('nome','categoria','descricao', 'valor', 'parcelas', 'valor_parcela',)
	list_filter = ('categoria', 'created',)
	# exclude = ('created',)

class MotoAdmin(admin.ModelAdmin):
	list_display = ('modelo', 'valor', 'categoria', 'cilindradas', 'ano', 'created',)
	list_filter = ('categoria', 'cilindradas', 'created',)
	# exclude = ('created',)

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Categoria)
admin.site.register(Cilindradas)
admin.site.register(MotoExtraInfo)
admin.site.register(Moto, MotoAdmin)
