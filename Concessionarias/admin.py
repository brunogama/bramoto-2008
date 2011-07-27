from django.contrib import admin
from models import Loja

class LojaAdmin(admin.ModelAdmin):
	list_display = ('cidade','nome', 'endereco', 'telefone',)
	# search_fields = ('chamada','texto',)
	# exclude = ('slug',)
	# exclude = ('slug',)
	list_filter = ('cidade','nome','created',)
	
	
admin.site.register(Loja, LojaAdmin)