from django.contrib import admin
from models import CaixaPostal


class CaixaPostalAdmin(admin.ModelAdmin):
    pass


admin.site.register(CaixaPostal)