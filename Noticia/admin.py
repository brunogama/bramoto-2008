# -*- encoding: latin-1 -*-

from django.contrib import admin
from models import Noticias

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('chamada', 'created')
	search_fields = ('chamada','texto',)
	fields = ('chamada', 'texto')

admin.site.register(Noticias, NoticiasAdmin)