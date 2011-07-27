from django.contrib import admin
from models import Banner

class BannerAdmin(admin.ModelAdmin):
	list_display = ('titulo','uri', 'banner', 'lado',)
	# search_fields = ('chamada','texto',)
	# exclude = ('slug',)
	# exclude = ('created',)
	list_filter = ('lado', 'created',)

admin.site.register(Banner, BannerAdmin)